import torch
import torch.nn as nn
import torch.nn.functional as F


class HybridModule(nn.Module):

    def __init__(self, query_max_size, core_term_size, core_term_embedding_size,
                 lstm_hidden_size=64, lstm_num_layers=2, margin=0.25):
        super(HybridModule, self).__init__()
        self.core_term_size = core_term_size
        self.core_term_embedding = nn.Embedding(core_term_size, core_term_embedding_size)
        self.margin = margin
        self.rnn = nn.LSTM(
            input_size=query_max_size + core_term_embedding_size,
            hidden_size=lstm_hidden_size,
            num_layers=lstm_num_layers,
            batch_first=True,
            bidirectional=True,
            dropout=0.05)
        self.fc = nn.Linear(lstm_hidden_size * 2, 1)

    def encode(self, matrix, length, core_terms):
        length = torch.cat(length)  # [batch_size * sample_size]
        _, idx_sort = torch.sort(length, dim=0, descending=True)
        _, idx_unsort = torch.sort(idx_sort, dim=0)
        length = length[idx_sort]

        # [batch_size * sample_size][code_max_size]
        core_terms = torch.cat([x.squeeze(dim=0) for x in torch.split(core_terms, 1)])
        # [batch_size * sample_size][code_max_size][core_term_embedding_size]
        core_term_vec = self.core_term_embedding(core_terms.long()).float()
        # [batch_size * sample_size][code_max_size][query_max_size]
        matrix = torch.cat([x.squeeze(dim=0) for x in torch.split(matrix, 1)]).float()

        # [batch_size * sample_size][code_max_size][query_max_size + core_term_embedding_size]
        x = torch.cat([matrix, core_term_vec], dim=2)
        x = x[idx_sort]
        x = torch.nn.utils.rnn.pack_padded_sequence(x, list(length), batch_first=True)
        # [batch_size * sample_size][time_steps][lstm_hidden_size * 2]
        x, _ = self.rnn(x)
        x, _ = torch.nn.utils.rnn.pad_packed_sequence(x, batch_first=True)
        index = length.view(-1, 1, 1)
        index = index.expand(x.shape[0], 1, x.shape[2]) - 1
        x = torch.gather(x, 1, index).squeeze()
        x = x[idx_unsort]
        out = self.fc(x).squeeze(1)
        return out

    def forward(self, pos_matrix, pos_core_terms, pos_lengths, neg_matrix, neg_core_terms, neg_lengths):
        pos_score = self.encode(pos_matrix, pos_lengths, pos_core_terms)
        neg_score = self.encode(neg_matrix, neg_lengths, neg_core_terms)
        k = int(neg_score.shape[0]/pos_score.shape[0])
        pos_score = pos_score.view(-1, 1).expand(pos_score.shape[0], k).contiguous().view(-1, 1).squeeze()
        loss = (self.margin - pos_score + neg_score).clamp(min=1e-6).mean()
        return loss

