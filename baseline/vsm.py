import warnings

from preprocess.lex.token import Tokenizer

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim import corpora, models, similarities


def vsm(data):
    documents = []
    for item in data:
        documents.append(item[0])
        documents.append(item[1])
    dictionary = corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(doc) for doc in documents]
    tfidf_model = models.TfidfModel(corpus)
    vectors = [tfidf_model[bow] for bow in corpus]
    sim = similarities.SparseMatrixSimilarity(tfidf_model[corpus],
                                              num_features=len(dictionary.keys()))
    mrr = 0
    hit = [0, 0, 0, 0, 0]
    for i in range(len(data)):
        query_id = i * 2
        query_tfidf = vectors[query_id]
        sim_result = sim[query_tfidf]
        rank = 0
        for id, item in enumerate(sim_result):
            if id % 2 == 1 and item >= sim_result[query_id + 1]:
                rank += 1
        mrr += 1.0 / rank
        for k in range(len(hit)):
            if rank <= k + 1:
                hit[k] += 1
        print(
            '#%d:' % int(data[i][2]), 'rank=%d' % rank, 'MRR=%.4f' % (mrr / (i + 1)),
            ', '.join([('Hit@%d=%.4f' % (k + 1, (h / (i + 1)))) for k, h in enumerate(hit)])
        )


if __name__ == '__main__':
    data = Tokenizer().parse('../data/domain/test.nl', '../data/domain/test.code')
    data = [item for item in data if len(item[0]) <= 20 and len(item[1]) <= 400]
    vsm(data)
