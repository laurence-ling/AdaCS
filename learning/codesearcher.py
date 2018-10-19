from __future__ import absolute_import

import os
import torch
import torch.optim as optim
from torch.utils.data import DataLoader
from tqdm import tqdm

from learning.model import HybridModule
from preprocess.dataset import CodeSearchDataset


class CodeSearcher:
    def __init__(self, conf):
        self.conf = conf
        self.wkdir = self.conf['data']['wkdir']

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
        self.model = model.cuda() if torch.cuda.is_available() else model

        save_round = int(self.conf['train']['save_round'])
        nb_epoch = int(self.conf['train']['nb_epoch'])
        batch_size = int(self.conf['train']['batch_size'])
        dataloader = DataLoader(self.trainset, batch_size=batch_size, shuffle=True)
        optimizer = optim.Adam(self.model.parameters(), lr=float(self.conf['train']['lr']))

        for epoch in range(nb_epoch):
            epoch_loss = 0
            for pos_matrix, pos_core_terms, pos_lengths, neg_matrix, neg_core_terms, neg_lengths in tqdm(dataloader):
                loss = self.model(gVar(pos_matrix), gVar(pos_core_terms), pos_lengths,
                                  gVar(neg_matrix), gVar(neg_core_terms), neg_lengths)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item()
            print('epoch', epoch, ': Loss =', epoch_loss/train_size)
            if epoch % save_round == 0:
                self.save_model(model, epoch)
        self.save_model(model, epoch)

def gVar(tensor):
    if torch.cuda.is_available():
        tensor = tensor.cuda()
    return tensor
