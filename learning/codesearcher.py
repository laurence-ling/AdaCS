from __future__ import absolute_import

import os
import numpy as np
import re
import torch
import torch.optim as optim
from torch.utils.data import DataLoader
from tqdm import tqdm

from learning.model.rnn import RnnModel
from preprocess.dataset import CodeSearchDataset
from preprocess.dataset import MatchingMatrix
from preprocess.lex.token import Tokenizer
from preprocess.lex.word_sim import WordSim


class CodeSearcher:
    def __init__(self, conf):
        self.conf = conf
        self.wkdir = self.conf['data']['wkdir']
        self.device = torch.device("cuda:2" if torch.cuda.is_available() else "cpu")
        train_data = CodeSearchDataset(os.path.join(conf['data']['wkdir'], conf['data']['train_db_path']))
        self.model = RnnModel(int(conf['data']['query_max_len']), train_data.core_term_size, int(conf['model']['core_term_embedding_size']), int(conf['model']['lstm_hidden_size']), int(conf['model']['lstm_layers']), float(self.conf['train']['margin'])).to(self.device)
        self.batch_size = int(self.conf['train']['batch_size'])

    def save_model(self, epoch):
        model_dir = os.path.join(self.wkdir, 'models')
        if not os.path.exists(model_dir):
            os.mkdir(model_dir)
        torch.save(self.model.state_dict(), os.path.join(model_dir, 'epoch%d.h5' % epoch))

    def load_model(self, epoch):
        model_path = os.path.join(self.wkdir, 'models/epoch%d.h5' % epoch)
        assert os.path.exists(model_path), 'Weights not found.'
        self.model.load_state_dict(torch.load(model_path, map_location=self.device))

    def train(self):
        train_data = CodeSearchDataset(os.path.join(self.wkdir, self.conf['data']['train_db_path']))
        valid_data = CodeSearchDataset(os.path.join(self.wkdir, self.conf['data']['valid_db_path']))
        test_data = CodeSearchDataset(os.path.join(self.wkdir, self.conf['data']['test_db_path']))
        train_size = len(train_data)
        if torch.cuda.device_count() > 1:
            print("let's use ", torch.cuda.device_count(), "GPUs")

        save_round = int(self.conf['train']['save_round'])
        nb_epoch = int(self.conf['train']['nb_epoch'])
        batch_size = self.batch_size
        dataloader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
        optimizer = optim.Adam(self.model.parameters(), lr=float(self.conf['train']['lr']))

        for epoch in range(nb_epoch):
            self.model.train()
            epoch_loss = 0
            for _, pos_matrix, pos_core_terms, pos_length, neg_matrix, neg_core_terms, neg_length, neg_ids in tqdm(dataloader):
                pos_length = [self.gVar(x) for x in pos_length]
                neg_length = [self.gVar(x) for x in neg_length]
                loss = self.model.loss(self.gVar(pos_matrix), self.gVar(pos_core_terms), pos_length,
                                  self.gVar(neg_matrix), self.gVar(neg_core_terms), neg_length)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item()
            print('epoch', epoch, ': Loss =', epoch_loss / (train_size/batch_size))
            if epoch % save_round == 0:
                self.save_model(epoch)
            print('Validation...')
            self.eval(valid_data)
            print('Test...')
            self.eval(test_data)

    def eval2(self):
        data = Tokenizer().parse(os.path.join(self.wkdir, self.conf['data']['test_nl_path']), os.path.join(self.wkdir, self.conf['data']['test_code_path']))
        fasttext_corpus_path = os.path.join(self.wkdir, re.sub(r'\.db$', '.txt', self.conf['data']['test_db_path']))
        core_term_path = os.path.join(self.wkdir, 'conf/core_terms.txt')
        word_sim = WordSim(core_term_path, pretrain=(self.conf['model']['pretrained_wordvec'] == str(True)), update=False, fasttext_corpus_path=fasttext_corpus_path)
        CodeSearchDataset.eval(self.model, data, word_sim, int(self.conf['data']['query_max_len']), int(self.conf['data']['code_max_len']), self.device)

    def eval(self, test_data):
        self.model.eval()
        batch_size = self.batch_size
        dataloader = DataLoader(test_data, batch_size=batch_size, shuffle=True)
        
        def top_k_acc(pos_score, neg_score, k):
            ranks = compute_rank(pos_score, neg_score)
            result = [1 for r in ranks if r <= k]
            count = sum(result)
            return count/len(ranks)

        def mrr(pos_score, neg_score):
            ranks = compute_rank(pos_score, neg_score)
            reciprocal = [1/r for r in ranks]
            return sum(reciprocal)/len(ranks)

        def compute_rank(pos_score, neg_score):
            ranks = [len(neg_score[0])+1]*len(pos_score)
            for i, pos_ in enumerate(pos_score):
                sort_neg_score = sorted(neg_score[i], reverse=True)
                for j, neg_ in enumerate(sort_neg_score):
                    if pos_ > neg_:
                        ranks[i] = j + 1
                        break
            return ranks

        top_k = 10
        accs = [[] for _ in range(top_k)]
        mrrs = []
        for q_id, pos_matrix, pos_core_terms, pos_length, neg_matrix, neg_core_terms, neg_length, neg_ids in dataloader:
            pos_length = [self.gVar(x) for x in pos_length]
            neg_length = [self.gVar(x) for x in neg_length]
            pos_score = self.model(self.gVar(pos_matrix), pos_length, self.gVar(pos_core_terms)).data.cpu().numpy()
            neg_score = self.model(self.gVar(neg_matrix), neg_length, self.gVar(neg_core_terms)).data.cpu().numpy()
            neg_score = np.split(neg_score, len(pos_score))
            for i in range(top_k):
                accs[i].append(top_k_acc(pos_score, neg_score, i+1))
            mrrs.append(mrr(pos_score, neg_score))
        for i in range(top_k):
            print('Hit@{}: {}'.format(i+1, np.mean(accs[i])))
        print('MRR: {}'.format(np.mean(mrrs)))

    def gVar(self, tensor):
        return tensor.to(self.device)

    def predict(self, output_file):
        tokenizer = Tokenizer()
        # {str: list} ->  {label: tokens}
        nl_dict = tokenizer.parse_nl(os.path.join(self.wkdir, self.conf['data']['test_nl_path']))
        code_dict = tokenizer.parse_code(os.path.join(self.wkdir, self.conf['data']['test_code_path']))
        fasttext_corpus_path = os.path.join(self.wkdir, re.sub(r'\.db$', '.txt', self.conf['data']['test_db_path']))
        core_term_path = os.path.join(self.wkdir, 'conf/core_terms.txt')
        word_sim = WordSim(core_term_path, pretrain=(self.conf['model']['pretrained_wordvec'] == str(True)), 
                           update=False, fasttext_corpus_path=fasttext_corpus_path)

        query_max_size = int(self.conf['data']['query_max_len'])
        code_max_size = int(self.conf['data']['code_max_len'])
        device = self.device
        self.model.eval()
        
        nl_data = [(nid, tokens[: query_max_size]) for (nid, tokens) in nl_dict.items()]
        code_data = [(cid, tokens[: code_max_size]) for (cid, tokens) in code_dict.items()]
        print(f'nl size: {len(nl_data)}, code size: {len(code_data)}')

        fout = open(output_file, 'w')
        for nid, nl_token in nl_data:
            items = []
            for cid, code_token in code_data:
                items.append(MatchingMatrix(nl_token, code_token, cid,
                                            word_sim, query_max_size))
            matrices = np.asarray([
                            [CodeSearchDataset.pad_matrix(np.transpose(item.matrix),
                                                          code_max_size,
                                                          query_max_size)]
                            for item in items])
            lengths = [torch.LongTensor([len(item.core_terms)]).to(device) for item in items]
            core_terms = np.asarray([
                                [CodeSearchDataset.pad_terms(item.core_terms, code_max_size)]
                            for item in items])
            output = self.model(torch.from_numpy(matrices).to(device),
                                lengths,
                                torch.from_numpy(core_terms).to(device))
            scores = output.cpu().detach().numpy().squeeze()
            print(f'nl {nid} writing...')
            for i, s in enumerate(scores):
                fout.write(f'{nid} {i + 1} {s}\n')
        fout.close()

