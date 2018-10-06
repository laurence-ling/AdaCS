import numpy
import os
import pickle
import random

from tokenization import Tokenizer
from word_process import WordSim


def negative_sampling(data):
    n = len(data)
    ret = []
    for i in range(n):
        k = i
        while k != i:
            k = random.randint(0, n - 1)
        ret.append((data[i][0], data[i][1], data[k][1]))
    return ret


def generate_data(data, word_sim, print_log=True):
    ret = []
    for i in range(len(data)):
        item = data[i]
        positive_matrix = generate_matrix(item[0], item[1], word_sim)
        positive_terms = generate_term_list(item[1], word_sim)
        negative_matrix = generate_matrix(item[0], item[2], word_sim)
        negative_terms = generate_term_list(item[2], word_sim)
        ret.append(((positive_matrix, positive_terms), (negative_matrix, negative_terms)))
        if print_log and i % 100 == 0:
            print('', i, '/', len(data))
    return ret


def generate_matrix(words_1, words_2, word_sim):
    ret = numpy.zeros([len(words_1), len(words_2)])
    for i in range(len(words_1)):
        for j in range(len(words_2)):
            ret[i][j] = word_sim.sim(words_1[i], words_2[j])
    return ret


def generate_term_list(words, word_sim):
    return [(word if word in word_sim.core_terms else '<UNK>') for word in words]


'''
output format:
    * train.pkl/dev.pkl: [ ( (positive_matrix, terms), (negative_matrix,terms) ) ]
        - each item in this list corresponds to a query;
        - positive_matrix: the relevance matching matrix of the query against its ground truth code snippet;
        - negative_matrix: the relevance matching matrix of the query against a randomly sampled negative code snippet;
        - terms: a list of terms in the code snippet, can be (1) core terms, or (2) <UNK> for unknown.
'''
if __name__ == '__main__':

    dataset_dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/xia18'))
    train_code_path = dataset_dir_path + '/train.code'
    train_nl_path = dataset_dir_path + '/train.nl'
    valid_code_path = dataset_dir_path + '/valid.code'
    valid_nl_path = dataset_dir_path + '/valid.nl'
    test_code_path = dataset_dir_path + '/test.code'
    test_nl_path = dataset_dir_path + '/test.nl'
    core_term_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../conf/core_terms.txt'))

    fasttext_corpus_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp/fasttext-corpus.txt'))
    train_output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp/train.pkl'))
    valid_output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp/valid.pkl'))

    train_data, valid_data, test_data = Tokenizer().parse(train_nl_path, valid_nl_path, test_nl_path, train_code_path,
                                                          valid_code_path, test_code_path)
    train_data = negative_sampling(train_data)
    valid_data = negative_sampling(valid_data)

    with open(fasttext_corpus_path, 'w') as f:
        for item in train_data:
            f.write(' '.join(item[0]) + '\n')
            f.write(' '.join(item[1]) + '\n')

    word_sim = WordSim(core_term_path)
    matrices = generate_data(train_data, word_sim)
    with open(train_output_path, 'wb') as f:
        pickle.dump(matrices, f)
    matrices = generate_data(valid_data, word_sim)
    with open(valid_output_path, 'wb') as f:
        pickle.dump(matrices, f)
