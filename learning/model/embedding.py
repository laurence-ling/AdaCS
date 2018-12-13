import torch
import torch.nn as nn


class CodeEmbeddingModule(nn.Module):

    def __init__(self, core_term_size, core_term_embedding_size):
        super(CodeEmbeddingModule, self).__init__()
        self.core_term_size = core_term_size
        x = self.core_term_size
        self.core_term_embedding = nn.Embedding(x, core_term_embedding_size)

    def forward(self, matrix, length, core_terms):
        length = torch.cat(length)  # [batch_size * sample_size]
        _, idx_sort = torch.sort(length, dim=0, descending=True)
        _, idx_unsort = torch.sort(idx_sort, dim=0)
        length = length[idx_sort]

        # [batch_size * sample_size][code_max_size]
        core_terms = torch.cat([x.squeeze(dim=0) for x in torch.split(core_terms, 1)])
        # [batch_size * sample_size][code_max_size][core_term_embedding_size]
        core_term_vec = self.core_term_embedding(core_terms.long()).float()
        # [batch_size * sample_size][code_max_size][query_max_size*2]
        matrix = torch.cat([x.squeeze(dim=0) for x in torch.split(matrix, 1)]).float()

        # [batch_size * sample_size][code_max_size][query_max_size*2 + core_term_embedding_size]
        x = torch.cat([matrix, core_term_vec], dim=2)
        x = x[idx_sort]
        return x, length, idx_unsort

