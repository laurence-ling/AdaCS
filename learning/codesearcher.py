import torch
import torch.nn as nn
from models import CNNEncoder
from configs import get_config
from dataset import CSDataset
import dataset
from torch.utils.data import DataLoader
import torch.optim as optim

class CodeSearcher:
    def __init__(self, conf):
        self.conf = conf
        self.model = CNNEncoder(self.conf['conv1_kernels'], self.conf['conv1_size'],
                                self.conf['pool1_target'], self.conf['conv2_kernels'],
                                self.conf['conv2_size'], self.conf['pool2_size'],
                                self.conf['fc1_units'], self.conf['fc2_units'])

    def train(self):
        nb_epoch = self.conf['nb_epoch']
        batch_size = self.conf['batch_size']
        trainset = CSDataset()
        data_loader = DataLoader(trainset, batch_size=batch_size, shuffle=True,
                                 num_workers=1) #collate_fn=dataset.collate_fn)
        criterion = nn.BCEWithLogitsLoss()
        optimizer = optim.Adam(self.model.parameters(), lr=0.01)
        for epoch in range(nb_epoch):
            for img, label in data_loader:
                logits = self.model(img)
                loss = criterion(logits, label)
                print(logits, loss)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()


if __name__ == '__main__':
    conf = get_config()
    searcher = CodeSearcher(conf)
    searcher.train()
