import numpy
from allennlp.modules.seq2seq_encoders import StackedSelfAttentionEncoder
from torch import nn

from learning.model.embedding import CodeEmbeddingModule


class TransformerModel(StackedSelfAttentionEncoder):

    def __init__(self, core_term_size, query_max_size, core_term_embedding_size, margin,
                 hidden_dim: int = 60, projection_dim=60, feedforward_hidden_dim=60,
                 num_heads: int = 4,
                 num_layers: int = 4) -> None:
        self.margin = margin
        self.input_dim = query_max_size * 2 + core_term_embedding_size
        super().__init__(self.input_dim, hidden_dim, projection_dim=projection_dim, feedforward_hidden_dim=feedforward_hidden_dim, num_layers=num_layers, num_attention_heads=num_heads)
        self.code_embedding = CodeEmbeddingModule(core_term_size, core_term_embedding_size)
        self.fc = nn.Linear(hidden_dim, 1)
        print('Transformer model, count(parameters)=%d' % (sum([numpy.prod(list(p.size())) for p in self.parameters()])))

    def forward(self, matrix, length, core_terms):
        h, _, idx_unsort = self.code_embedding(matrix, length, core_terms)
        h = h[idx_unsort]
        h = super().forward(h, None)
        return self.fc(h[:, -1, :].squeeze())

    def loss(self, pos_matrix, pos_core_terms, pos_lengths, neg_matrix, neg_core_terms, neg_lengths):
        pos_score = self.forward(pos_matrix, pos_lengths, pos_core_terms)
        neg_score = self.forward(neg_matrix, neg_lengths, neg_core_terms)
        k = int(neg_score.shape[0]/pos_score.shape[0])
        pos_score = pos_score.view(-1, 1).expand(-1, k).contiguous().view(-1, 1).squeeze()
        loss = (self.margin - pos_score + neg_score).clamp(min=1e-6).mean()
        return loss
