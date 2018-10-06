import os, numpy, functools
from scipy import spatial
from fastText import train_unsupervised

class WordSim:

    def __init__(self, core_term_path):
        self.word_embeddings = WordEmbeddings()
        with open(core_term_path, 'r') as f:
            self.core_terms = set([word for word in f.readlines() if len(word) > 0])

    @functools.lru_cache(maxsize= 64 * 1024, typed=False)
    def sim(self, word_1, word_2):
        vec_1 = self.word_embeddings[word_1]
        vec_2 = self.word_embeddings[word_2]
        return spatial.distance.cosine(vec_1, vec_2)

class WordEmbeddings:

    def __init__(self):
        data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp/fasttext-corpus.txt'))
        self.model = train_unsupervised(input = data_path, model = 'skipgram')
    
    @functools.lru_cache(maxsize=None, typed=False)
    def __getitem__(self, word):
        return self.model.get_word_vector(word)