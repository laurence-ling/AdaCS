import torch
import torch.nn as nn
import torch.nn.functional as F


class HybridModule(nn.Module):

    def __init__(self, query_max_size, core_term_size, core_term_embedding_size,
                 lstm_hidden_size=64, lstm_num_layers=2, fc_hidden_size=28):
        self.core_term_size = core_term_size
        self.core_term_embedding = nn.Embedding(core_term_size, core_term_embedding_size)
        self.rnn = nn.LSTM(
            input_size=query_max_size + core_term_embedding_size,
            hidden_size=lstm_hidden_size,
            num_layers=lstm_num_layers,
            batch_first=True,
            bidirectional=True)

        self.fc_1 = nn.Linear(lstm_hidden_size * 2, fc_hidden_size)
        self.fc_2 = nn.Linear(fc_hidden_size, 1)

    def encode(self, item):
        sim_vec = item[0]
        core_term_idx = item[1]
        core_term_vec = self.core_term_embedding(
            torch.zeros(1, self.core_term_size).scatter_(1, core_term_idx, 1).squeeze())
        x = torch.cat([sim_vec, core_term_vec])
        print(x.size())
        seq_len, emb_size = x.size()
        x = x.unsqueeze(0)
        rnn_out, _ = self.rnn(x, None) # batch_sz x seq_len x hidden_sz*2
        #rnn_out = F.maxpool1d(rnn_out.transpose(1, 2), seq_len).sequeeze(2) # batch_sz x hidden_sz*2
        rnn_out = rnn_out[:, -1, :] # use the last output state, batch_sz x hidden_sz*2
        x = F.dropout(rnn_out, 0.25, self.training)
        x = rnn_out[:, -1, :]
        x = F.relu(self.fc_1(x))
        output = F.sigmoid(self.fc_2(x))
        return output

    def forward(self, pos_sample, neg_sample):
        batch_size = len(pos_sample) # for varible length samples, batch_size=1
        pos_score = self.encode(pos_sample)
        neg_score = self.encode(neg_sample)
        loss = (self.margin-pos_score+neg_score).clamp(min=1e-6).mean()
        return loss

