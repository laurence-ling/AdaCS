import numpy
import torch
import torch.nn as nn
import torch.nn.functional as F

from learning.model.embedding import CodeEmbeddingModule


class RnnModel(nn.Module):

    def __init__(self, query_max_size, core_term_size, core_term_embedding_size,
                 lstm_hidden_size=64, lstm_num_layers=2, margin=0.25):
        super(RnnModel, self).__init__()
        self.code_embedding = CodeEmbeddingModule(core_term_size, core_term_embedding_size)
        self.margin = margin
        self.rnn = nn.LSTM(
            input_size=query_max_size * 2 + core_term_embedding_size,
            hidden_size=lstm_hidden_size,
            num_layers=lstm_num_layers,
            batch_first=True,
            bidirectional=False,
            dropout=0.05)
        self.fc = nn.Linear(lstm_hidden_size, 1)
        print('RNN model, count(parameters)=%d' % (sum([numpy.prod(list(p.size())) for p in self.parameters()])))

    def forward(self, matrix, length, core_terms):
        x, length, idx_unsort = self.code_embedding(matrix, length, core_terms)
        x = torch.nn.utils.rnn.pack_padded_sequence(x, list(length), batch_first=True)
        # [batch_size * sample_size][time_steps][lstm_hidden_size * 2]
        x, _ = self.rnn(x)
        x, _ = torch.nn.utils.rnn.pad_packed_sequence(x, batch_first=True)
        # print(x)
        index = length.view(-1, 1, 1)
        index = index.expand(x.shape[0], 1, x.shape[2]) - 1
        x = torch.gather(x, 1, index).squeeze()
        x = x[idx_unsort]
        out = self.fc(x).squeeze(1)
        return out

    def loss(self, pos_matrix, pos_core_terms, pos_lengths, neg_matrix, neg_core_terms, neg_lengths):
        pos_score = self.forward(pos_matrix, pos_lengths, pos_core_terms)
        neg_score = self.forward(neg_matrix, neg_lengths, neg_core_terms)
        k = int(neg_score.shape[0]/pos_score.shape[0])
        pos_score = pos_score.view(-1, 1).expand(pos_score.shape[0], k).contiguous().view(-1, 1).squeeze()
        loss = (self.margin - pos_score + neg_score).clamp(min=1e-6).mean()
        return loss

