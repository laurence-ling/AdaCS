import configparser
import torch
import torch.optim as optim
from learning.model import HybridModule
from data_preprocess.dataset import CodeSearchDataset
from tqdm import tqdm


class CodeSearcher:
    def __init__(self, conf):
        self.conf = conf
        self.trainset = CodeSearchDataset('../tmp/valid.db')
        self.query_max_size = self.trainset.query_max_size
        self.core_term_size = self.trainset.core_term_size
        self.batch_size = int(self.conf['train']['batch_size'])
        self.model = HybridModule(
            self.query_max_size, self.core_term_size,
            int(self.conf['model']['core_term_embedding_size']), int(self.conf['model']['lstm_layers']),
            int(self.conf['model']['lstm_hidden_size']), int(self.conf['model']['fc_hidden_size']), float(self.conf['train']['margin']))

    def train(self):
        nb_epoch = int(self.conf['train']['nb_epoch'])

        optimizer = optim.Adam(self.model.parameters(), lr=float(self.conf['train']['lr']))
        train_size = len(self.trainset)
        for epoch in range(nb_epoch):
            shuffle_index = torch.randperm(train_size).tolist()
            epoch_loss = 0
            iter_data = [shuffle_index[i:i + self.batch_size] for i in range(0, len(shuffle_index), self.batch_size)]
            for index_list in tqdm(iter_data):
                loss = 0
                for i in index_list:
                    sample = self.trainset[i]
                    pos_sample = sample.pos_data
                    for neg_sample in sample.neg_data_list:
                        loss += self.model(pos_sample, neg_sample)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item()
            print('epoch', epoch, ': Loss =', epoch_loss/train_size)


def get_config():
    config = configparser.ConfigParser()
    config.read('../conf/config.ini')
    return config


if __name__ == '__main__':
    conf = get_config()
    searcher = CodeSearcher(conf)
    searcher.train()
