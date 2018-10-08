import random
import warnings

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim import corpora, models, similarities


class BowSimilarity:

    def __init__(self, documents):
        dictionary = corpora.Dictionary(documents)
        corpus = [dictionary.doc2bow(doc) for doc in documents]
        tfidf_model = models.TfidfModel(corpus)
        self.vectors = [tfidf_model[bow] for bow in corpus]
        self.sim = similarities.SparseMatrixSimilarity(tfidf_model[corpus],
                                                       num_features=len(dictionary.keys()))

    def negative_sampling(self, query_id, top_k, sampling_size):
        results = [item[0] for item in self.__search(query_id, top_k) if item[0] != query_id]
        random.shuffle(results)
        return results[:sampling_size]

    def __search(self, query_id, top_k):
        query_tfidf = self.vectors[query_id]
        sim = self.sim[query_tfidf]
        return sorted(enumerate(sim), key=lambda item: -item[1])[:top_k]
