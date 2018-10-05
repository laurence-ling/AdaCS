import os, random, numpy, pickle
import tokenization, word_process

def negative_sampling(data):
    n = len(data)
    ret = []
    for i in range(n):
        k = i
        while k != i:
            k = random.randint(0, n-1)
        ret.append((data[i][0], data[i][1], data[k][1]))
    return ret

def generate_matrices(data, word_sim, print_log = True):
    ret = []
    for i in range(len(data)):
        item = data[i]
        positive_matrix = generate_matrix(item[0], item[1], word_sim)
        negative_matrix = generate_matrix(item[0], item[2], word_sim)
        ret.append((positive_matrix, negative_matrix))
        if print_log and i % 100 ==0:
            print('', i, '/', len(data))
    return ret
    
def generate_matrix(words_1, words_2, word_sim):
    ret = numpy.zeros([len(words_1), len(words_2)])
    for i in range(len(words_1)):
        for j in range(len(words_2)):
            ret[i][j] = word_sim.sim(words_1[i], words_2[j])
    return ret

'''
output format:
    * train.pkl/dev.pkl: [(positive_matrix, negative_matrix)]
        - each item in this list corresponds to a query;
        - positive_matrix: the relevance matching matrix of the query against its ground truth code snippet;
        - negative_matrix: the relevance matching matrix of the query against a randomly sampled negative code snippet.
'''
if __name__ == '__main__':

    dataset_dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/xia18'))
    train_code_path = dataset_dir_path + '/train.code'
    train_nl_path = dataset_dir_path + '/train.nl'
    valid_code_path = dataset_dir_path + '/valid.code'
    valid_nl_path = dataset_dir_path + '/valid.nl'
    test_code_path = dataset_dir_path + '/test.code'
    test_nl_path = dataset_dir_path + '/test.nl'

    fasttext_corpus_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp/fasttext-corpus.txt'))
    train_output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp/train.pkl'))
    dev_output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp/train.pkl'))

    train_data, dev_data, test_data = tokenization.parse(train_nl_path, valid_nl_path, test_nl_path, train_code_path, valid_code_path, test_code_path)
    train_data = negative_sampling(train_data)
    dev_data = negative_sampling(dev_data)

    with open(fasttext_corpus_path, 'w') as f:
        for item in train_data:
            f.write(' '.join(item[0]) + '\n')
            f.write(' '.join(item[1]) + '\n')
    
    word_sim = word_process.WordSim()
    matrices = generate_matrices(train_data, word_sim)
    with open(train_output_path, 'wb') as f:
        pickle.dump(matrices, f)
    matrices = generate_matrices(dev_data, word_sim)
    with open(dev_output_path, 'wb') as f:
        pickle.dump(matrices, f)