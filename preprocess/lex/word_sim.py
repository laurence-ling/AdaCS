import functools

from fastText import train_unsupervised
from scipy import spatial


class WordSim:

    def __init__(self, core_term_path, fasttext_corpus_path):
        with open(core_term_path, 'r') as f:
            self.core_terms = set([word.strip() for word in f.readlines() if len(word.strip()) > 0])
        # print(self.core_terms)
        self.word_embeddings = WordEmbeddings(fasttext_corpus_path)
        self.core_term_dict = {}
        index = 2
        for core_term in self.core_terms:
            self.core_term_dict[core_term] = index
            index += 1

    @functools.lru_cache(maxsize=64 * 1024, typed=False)
    def sim(self, word_1, word_2):
        vec_1 = self.word_embeddings[word_1]
        vec_2 = self.word_embeddings[word_2]
        return 1.0 - spatial.distance.cosine(vec_1, vec_2)


class WordEmbeddings:

    def __init__(self, fasttext_corpus_path):
        self.model = train_unsupervised(input=fasttext_corpus_path, model='skipgram')

    @functools.lru_cache(maxsize=None, typed=False)
    def __getitem__(self, word):
        return self.model.get_word_vector(word)
