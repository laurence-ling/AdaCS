from __future__ import absolute_import

import os
import numpy as np
import torch
import torch.optim as optim
from torch.utils.data import DataLoader
from tqdm import tqdm

from learning.model import HybridModule
from preprocess.dataset import CodeSearchDataset
from preprocess.lex.token import Tokenizer
from preprocess.lex.word_sim import WordSim


class CodeSearcher:
    def __init__(self, conf):
        self.conf = conf
        self.wkdir = self.conf['data']['wkdir']
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        train_data = CodeSearchDataset(os.path.join(conf['data']['wkdir'], conf['data']['train_db_path']))
        self.model = HybridModule(
            int(conf['data']['query_max_len']), train_data.core_term_size,
            int(conf['model']['core_term_embedding_size']),
            int(conf['model']['lstm_hidden_size']),
            int(conf['model']['lstm_layers']),
            float(self.conf['train']['margin'])).to(self.device)

    def save_model(self, epoch):
        model_dir = os.path.join(self.wkdir, 'models')
        if not os.path.exists(model_dir):
            os.mkdir(model_dir)
        torch.save(self.model.state_dict(), os.path.join(model_dir, 'epoch%d.h5' % epoch))

    def load_model(self, epoch):
        model_path = os.path.join(self.wkdir, 'models/epoch%d.h5' % epoch)
        assert os.path.exists(model_path), 'Weights not found.'
        self.model.load_state_dict(torch.load(model_path))

    def train(self):
        train_data = CodeSearchDataset(os.path.join(self.wkdir, self.conf['data']['train_db_path']))
        valid_data = CodeSearchDataset(os.path.join(self.wkdir, self.conf['data']['valid_db_path']))
        test_data = CodeSearchDataset(os.path.join(self.wkdir, self.conf['data']['test_db_path']))
        train_size = len(train_data)
        if torch.cuda.device_count() > 1:
            print("let's use ", torch.cuda.device_count(), "GPUs")

        save_round = int(self.conf['train']['save_round'])
        nb_epoch = int(self.conf['train']['nb_epoch'])
        batch_size = int(self.conf['train']['batch_size'])
        dataloader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
        optimizer = optim.Adam(self.model.parameters(), lr=float(self.conf['train']['lr']))

        for epoch in range(nb_epoch):
            epoch_loss = 0
            for _, pos_matrix, pos_core_terms, pos_length, neg_matrix, neg_core_terms, neg_length, neg_ids in tqdm(dataloader):
                pos_length = [self.gVar(x) for x in pos_length]
                neg_length = [self.gVar(x) for x in neg_length]
                loss = self.model(self.gVar(pos_matrix), self.gVar(pos_core_terms), pos_length,
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
            self.model.train()

    def eval2(self):
        data = Tokenizer().parse(os.path.join(self.wkdir, self.conf['data']['test_nl_path']), os.path.join(self.wkdir, self.conf['data']['test_code_path']))
        fasttext_corpus_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp/fasttext-corpus-current.txt'))
        core_term_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../conf/core_terms.txt'))
        word_sim = WordSim(core_term_path, fasttext_corpus_path, False)
        CodeSearchDataset.eval(self.model, data, word_sim, int(self.conf['data']['query_max_len']), int(self.conf['data']['code_max_len']), self.device)

    def eval(self, test_data):
        self.model.eval()
        batch_size = int(self.conf['train']['batch_size'])
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

        top_k = 5
        accs = [[] for _ in range(top_k)]
        mrrs = []
        for q_id, pos_matrix, pos_core_terms, pos_length, neg_matrix, neg_core_terms, neg_length, neg_ids in dataloader:
            pos_length = [self.gVar(x) for x in pos_length]
            neg_length = [self.gVar(x) for x in neg_length]
            pos_score = self.model.encode(self.gVar(pos_matrix), pos_length, self.gVar(pos_core_terms)).data.cpu().numpy()
            neg_score = self.model.encode(self.gVar(neg_matrix), neg_length, self.gVar(neg_core_terms)).data.cpu().numpy()
            neg_score = np.split(neg_score, len(pos_score))
            for i in range(top_k):
                accs[i].append(top_k_acc(pos_score, neg_score, i+1))
            mrrs.append(mrr(pos_score, neg_score))
        for i in range(top_k):
            print('Hit@{}: {}'.format(i+1, np.mean(accs[i])))
        print('MRR: {}'.format(np.mean(mrrs)))

    def gVar(self, tensor):
        return tensor.to(self.device)

