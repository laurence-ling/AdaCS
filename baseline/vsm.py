import warnings

from preprocess.lex.token import Tokenizer
from gensim.parsing.porter import PorterStemmer

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim import corpora, models, similarities


def vsm(data):
    p = PorterStemmer()
    documents = []
    for item in data:
        documents.append([p.stem(w) for w in item[0]])
        documents.append([p.stem(w) for w in item[1]])
    dictionary = corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(doc) for doc in documents]
    tfidf_model = models.TfidfModel(corpus)
    vectors = [tfidf_model[bow] for bow in corpus]
    sim = similarities.SparseMatrixSimilarity(tfidf_model[corpus],
                                              num_features=len(dictionary.keys()))
    mrr = 0
    for i in range(len(data)):
        query_id = i * 2
        query_tfidf = vectors[query_id]
        sim_result = sim[query_tfidf]
        rank = 0
        for id, item in enumerate(sim_result):
            if id % 2 == 1 and item >= sim_result[query_id + 1]:
                rank += 1
        print('#%d:' % int(data[i][2]), 'rank=%d' % rank)
        mrr += 1.0 / rank
    mrr /= len(data)
    print(mrr)


if __name__ == '__main__':
    data = Tokenizer().parse('../data/domain/test.nl', '../data/domain/test.code')
    data = [item for item in data if len(item[0]) <= 20 and len(item[1]) <= 400]
    vsm(data)
