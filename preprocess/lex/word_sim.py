import functools
import fastText
import re, os

from gensim import corpora, models
from gensim.parsing import PorterStemmer
from scipy import spatial


class WordSim:

    def __init__(self, core_term_path, pretrain=True, update=True, fasttext_corpus_path=None):
        p = PorterStemmer()
        with open(core_term_path, 'r') as f:
            self.core_terms = list(set([p.stem(word.strip()) for word in f.readlines() if len(word.strip()) > 0]))
            self.core_terms.sort()
        self.word_embeddings = WordEmbeddings(pretrain, update, fasttext_corpus_path)
        self.core_term_dict = {}
        index = 2
        for core_term in self.core_terms:
            self.core_term_dict[core_term] = index
            index += 1
        with open(fasttext_corpus_path, 'r') as f:
            fasttext_corpus_content = f.readlines()
        documents = [line.strip().split() for idx, line in enumerate(fasttext_corpus_content) if idx % 2 ==0 and len(line.strip()) > 0]
        dictionary = corpora.Dictionary(documents)
        corpus = [dictionary.doc2bow(doc) for doc in documents]
        tfidf_model = models.TfidfModel(corpus)
        self.idfs = {dictionary[kv[0]]: kv[1] for kv in tfidf_model.idfs.items()}

    def idf(self, word):
        if word in self.idfs.keys():
            return self.idfs[word]
        else:
            return 1.0

    @functools.lru_cache(maxsize=64 * 1024, typed=False)
    def sim(self, word_1, word_2):
        vec_1 = self.word_embeddings[word_1]
        vec_2 = self.word_embeddings[word_2]
        return 1.0 - spatial.distance.cosine(vec_1, vec_2)


class WordEmbeddings:

    def __init__(self, pretrain=True, update=True, fasttext_corpus_path=None):
        if pretrain:
            self.model = fastText.load_model('resource/cc.en.300.bin')
            return
        model_path = re.sub(r'\.txt$', '.model', fasttext_corpus_path)
        if update or not os.path.exists(model_path):
            self.model = fastText.train_unsupervised(input=fasttext_corpus_path, model='skipgram')
            self.model.save_model(model_path)
        else:
            self.model = fastText.load_model(model_path)

    @functools.lru_cache(maxsize=None, typed=False)
    def __getitem__(self, word):
        return self.model.get_word_vector(word)
