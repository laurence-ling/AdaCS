from __future__ import absolute_import

import os
import configparser
import torch
import torch.optim as optim
from tqdm import tqdm

from learning.model import HybridModule
from preprocess.dataset import CodeSearchDataset
from preprocess import dataset


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
        optimizer = optim.Adam(self.model.parameters(), lr=float(self.conf['train']['lr']))

        for epoch in range(nb_epoch):
            shuffle_index = torch.randperm(train_size).tolist()
            epoch_loss = 0
            batch_iter = [shuffle_index[i: i+batch_size] for i in range(0, train_size, batch_size)]
            for batch_index in tqdm(batch_iter):
                loss = 0
                for i in batch_index:
                    sample = self.trainset[i]
                    pos_sample = sample.pos_data
                    for neg_sample in sample.neg_data_list:
                        loss += self.model(pos_sample, neg_sample)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item()
            print('epoch', epoch, ': Loss =', epoch_loss/train_size)
            if epoch % save_round == 0:
                self.save_model(model, epoch)


def get_config():
    config = configparser.ConfigParser()
    config.read('../conf/config.ini')
    return config


if __name__ == '__main__':
    conf = get_config()
    searcher = CodeSearcher(conf)
    searcher.train()
