import torch
import torch.nn as nn


class CodeEmbeddingModule(nn.Module):

    def __init__(self, core_term_size, core_term_embedding_size, position=False, code_max_size=0):
        super(CodeEmbeddingModule, self).__init__()
        self.position = position
        self.core_term_size = core_term_size
        x = self.core_term_size
        if position:
            x += code_max_size
        self.core_term_embedding = nn.Embedding(x, core_term_embedding_size)

    def forward(self, matrix, length, core_terms):
        length = torch.cat(length)  # [batch_size * sample_size]
        _, idx_sort = torch.sort(length, dim=0, descending=True)
        _, idx_unsort = torch.sort(idx_sort, dim=0)
        length = length[idx_sort]

        # [batch_size * sample_size][code_max_size]
        core_terms = torch.cat([x.squeeze(dim=0) for x in torch.split(core_terms, 1)])
        if self.position:
            core_terms = torch.unsqueeze(core_terms, 2).expand(core_terms.shape[0], core_terms.shape[1], 2)
            for i in range(core_terms.shape[0]):
                for j in range(core_terms.shape[1]):
                    core_terms[i][j][1] = self.core_term_size + j
        # [batch_size * sample_size][code_max_size][core_term_embedding_size]
        core_term_vec = self.core_term_embedding(core_terms.long()).float()
        if self.position:
            core_term_vec = core_term_vec.sum(dim=2)
        # [batch_size * sample_size][code_max_size][query_max_size*2]
        matrix = torch.cat([x.squeeze(dim=0) for x in torch.split(matrix, 1)]).float()

        # [batch_size * sample_size][code_max_size][query_max_size*2 + core_term_embedding_size]
        x = torch.cat([matrix, core_term_vec], dim=2)
        x = x[idx_sort]
        return x, length, idx_unsort

