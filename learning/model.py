import torch
import torch.nn as nn
import torch.nn.functional as F


class HybridModule(nn.Module):

    def __init__(self, query_max_size, core_term_size, core_term_embedding_size,
                 lstm_hidden_size=64, lstm_num_layers=2, fc_hidden_size=28, margin=0.25):
        super(HybridModule, self).__init__()
        self.core_term_size = core_term_size
        self.core_term_embedding = nn.Embedding(core_term_size, core_term_embedding_size)
        self.margin = margin
        self.rnn = nn.LSTM(
            input_size=query_max_size + core_term_embedding_size,
            hidden_size=lstm_hidden_size,
            num_layers=lstm_num_layers,
            batch_first=True,
            bidirectional=True)

        self.fc = nn.Linear(lstm_hidden_size * 2, 1)

    def encode(self, matrix, length, core_terms):
        core_terms = torch.cat([x.squeeze(dim=0) for x in torch.split(core_terms, 1)])
        matrix = torch.cat([x.squeeze(dim=0) for x in torch.split(matrix, 1)]).float()
        core_term_vec = self.core_term_embedding(core_terms.long()).float()
        x = torch.cat([matrix, core_term_vec], dim=2)
        length = torch.cat(length)
        _, idx_sort = torch.sort(length, dim=0, descending=True)
        x = x.index_select(0, idx_sort)
        length = list(length[idx_sort])
        x = torch.nn.utils.rnn.pack_padded_sequence(x, length, batch_first=True)
        # batch_size, seq_len, emb_size = x.size()
        x, _ = self.rnn(x, None) # batch_sz x seq_len x hidden_sz*2
        x, _ = torch.nn.utils.rnn.pad_packed_sequence(x, batch_first=True)
        # rnn_out = F.maxpool1d(rnn_out.transpose(1, 2), seq_len).sequeeze(2) # batch_sz x hidden_sz*2
        x = x[:, -1, :]  # use the last output state, batch_sz x hidden_sz*2
        x = F.dropout(x, 0.25, self.training)
        x = torch.tanh(self.fc(x))
        return x

    def forward(self, pos_matrix, pos_core_terms, pos_lengths, neg_matrix, neg_core_terms, neg_lengths):
        pos_score = self.encode(pos_matrix, pos_lengths, pos_core_terms)
        neg_score = self.encode(neg_matrix, neg_lengths, neg_core_terms)
        neg_sample_count = int(neg_score.shape[0] / pos_score.shape[0])
        pos_score = torch.cat([pos_score] * neg_sample_count).view(neg_sample_count, -1)\
            .permute(1, 0).contiguous().view(-1)
        loss = (self.margin-pos_score+neg_score).clamp(min=1e-6).mean()
        return loss

