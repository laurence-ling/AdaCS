import configparser

import torch
import torch.nn as nn
import torch.optim as optim

from models import HybridModule
from data_preprocess.dataset import CodeSearchDataset
from torch.utils.data import DataLoader

class CodeSearcher:
    def __init__(self, conf):
        self.conf = conf
        self.trainset = CodeSearchDataset('../tmp/train.pk')
        self.query_max_size = self.trainset.query_max_size
        self.core_term_size = self.trainset.core_term_size
        self.model = HybridModule(
                self.query_max_size, self.core_term_size, 
                self.conf['model']['core_term_embedding_size'],self.conf['model']['lstm_layers'],
                self.conf['model']['lstm_hidden_size'], self.conf['model']['fc_hidden_size'])

    def train(self):
        nb_epoch = self.conf['train']['nb_epoch']
        batch_size = self.conf['train']['batch_size']
    
        #data_loader = DataLoader(trainset, batch_size=batch_size, shuffle=True,
        #                         num_workers=1) #collate_fn=dataset.collate_fn)
        optimizer = optim.Adam(self.model.parameters(), lr=self.conf['train']['lr']
        train_size = len(self.trainset)
        for epoch in range(nb_epoch):
            shuffle_index = torch.randperm(train_size).tolist
            loss = 0
            for i, index in enumerate(shuffle_index):
                sample = self.trainset[i]
                pos_sample = sample.pos_data
                for neg_sample in sample.neg_data_list:
                    loss += model(pos_sample, neg_sample)
                    print(loss)
                if i % 8 == 0:
                    optimizer.zero_grad()
                    loss.backward()
                    optimizer.step()
                    loss = 0

def get_config():
    config = configparser()
    config.read('../conf/config.ini')
    return config

if __name__ == '__main__':
    conf = get_config()
    searcher = CodeSearcher(conf)
    searcher.train()
