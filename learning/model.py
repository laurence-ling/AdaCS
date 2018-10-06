import torch
import torch.nn as nn
import torch.nn.functional as F


class HybridModule(nn.Module):

    def __init__(self, relevancy_size, core_term_size, core_term_embedding_size,
                 lstm_hidden_size=64, lstm_num_layers=2, fc_hidden_size=28
                 ):
        self.core_term_size = core_term_size
        self.core_term_embedding = nn.Embedding(core_term_size, core_term_embedding_size)
        self.rnn = nn.LSTM(
            input_size=relevancy_size + core_term_embedding_size,
            hidden_size=lstm_hidden_size,
            num_layers=lstm_num_layers,
            batch_first=True,
            bidirectional=True
        )

        self.fc_activation = F.relu
        self.fc_1 = nn.Linear(lstm_hidden_size * 2, fc_hidden_size)
        self.fc_2 = nn.Linear(fc_hidden_size, 1)

    def forward(self, items):
        ret = 0
        for item in items:
            sim_vec = item[0]
            core_term_idx = item[1]
            core_term_vec = self.core_term_embedding(
                torch.zeros(1, self.core_term_size).scatter_(1, core_term_idx, 1).squeeze())
            x = torch.cat([sim_vec, core_term_vec])
            r_out, _ = self.rnn(x, None)
            data = r_out[:, -1, :]
            data = self.fc_1(data)
            data = self.fc_activation(data)
            data = self.fc_2(data)
            data = self.fc_activation(data)
            ret += F.dropout(data, 0.25, self.training)
        return ret
