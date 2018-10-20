from __future__ import absolute_import

import os
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from tqdm import tqdm

from learning.model import HybridModule
from preprocess.dataset import CodeSearchDataset


class CodeSearcher:
    def __init__(self, conf):
        self.conf = conf
        self.wkdir = self.conf['data']['wkdir']
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    def save_model(self, model, epoch):
        model_dir = self.wkdir + 'models/'
        if not os.path.exists(model_dir):
            os.mkdir(model_dir)
        torch.save(model.state_dict(), model_dir +'/epoch%d.h5' % epoch)

    def load_model(self, model, epoch):
        assert os.path.exists(self.wkdir+'models/epoch%d.h5'%epoch), 'Weights not found.'
        model.load_state_dict(torch.load(self.wkdir+'models/epoch%d.h5'%epoch))

    def train(self):
        self.trainset = CodeSearchDataset(os.path.join(self.wkdir, './tmp/valid.db'))
        train_size = len(self.trainset)
        self.query_max_size = self.trainset.query_max_size
        self.core_term_size = self.trainset.core_term_size
        model = HybridModule(
            self.query_max_size, self.core_term_size,
            int(self.conf['model']['core_term_embedding_size']), int(self.conf['model']['lstm_layers']),
            int(self.conf['model']['lstm_hidden_size']), int(self.conf['model']['fc_hidden_size']),
            float(self.conf['train']['margin']))
        if torch.cuda.device_count() > 1:
            print("let's use ", torch.cuda.device_count(), "GPUs")
            #model = nn.DataParallel(model)
        self.model = model.to(self.device)

        save_round = int(self.conf['train']['save_round'])
        nb_epoch = int(self.conf['train']['nb_epoch'])
        batch_size = int(self.conf['train']['batch_size'])
        dataloader = DataLoader(self.trainset, batch_size=batch_size, shuffle=True)
        optimizer = optim.Adam(self.model.parameters(), lr=float(self.conf['train']['lr']))

        for epoch in range(nb_epoch):
            epoch_loss = 0
            for pos_matrix, pos_core_terms, pos_length, neg_matrix, neg_core_terms, neg_length in tqdm(dataloader):
                pos_length = [self.gVar(x) for x in pos_length]
                neg_length = [self.gVar(x) for x in neg_length]
                loss = self.model(self.gVar(pos_matrix), self.gVar(pos_core_terms), pos_length,
                                  self.gVar(neg_matrix), self.gVar(neg_core_terms), neg_length)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item()
            print('epoch', epoch, ': Loss =', epoch_loss / train_size)
            if epoch % save_round == 0:
                self.save_model(model, epoch)
            self.model.eval()
            self.eval('tmp/valid.db')
            self.model.train()

    def eval(self, db_path, print_log=False):
        test_data = CodeSearchDataset(os.path.join(self.wkdir, db_path))
        if print_log:
            test_size = len(test_data)
            print('start eval... testset size: ', test_size)
        batch_size = int(self.conf['train']['batch_size'])
        dataloader = DataLoader(test_data, batch_size=len(test_data), shuffle=True)
        
        def top1_acc(pos_score, neg_score):
            samples = len(pos_score)
            count = 0
            for i, pos_n in enumerate(pos_score):
                if pos_n > neg_score[i].max():
                    count += 1
            return count/samples
        
        accs = []
        for pos_matrix, pos_core_terms, pos_length, neg_matrix, neg_core_terms, neg_length in dataloader:
            pos_length = [self.gVar(x) for x in pos_length]
            neg_length = [self.gVar(x) for x in neg_length]
            pos_score = self.model.encode(self.gVar(pos_matrix), pos_length, self.gVar(pos_core_terms)).data.numpy()
            neg_score = self.model.encode(self.gVar(neg_matrix), neg_length, self.gVar(neg_core_terms)).data.numpy()
            pos_score, neg_score = pos_score.squeeze(1), neg_score.squeeze(1)
            K = int(neg_score.shape[0] / pos_score.shape[0])
            neg_score = np.split(neg_score, len(pos_score))
            acc = top1_acc(pos_score, neg_score)
            accs.append(acc)
        print('ACC: {}'.format(np.mean(accs)))

    def gVar(self, tensor):
        return tensor.to(self.device)
