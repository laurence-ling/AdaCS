import os
from data_preprocess.lex.token import Tokenizer
from data_preprocess.lex.word_sim import WordSim
from data_preprocess.dataset import CodeSearchDataset


'''
output format:
    * train.pkl/dev.pkl: [ ( (positive_matrix, terms), (negative_matrix,terms) ) ]
        - each item in this list corresponds to a query;
        - positive_matrix: the relevance matching matrix of the query against its ground truth code snippet;
        - negative_matrix: the relevance matching matrix of the query against a randomly sampled negative code snippet;
        - terms: a list of terms indices in the code snippet.
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
    train_db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp/train.db'))
    valid_db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp/valid.db'))

    train_data = Tokenizer().parse(train_nl_path, train_code_path)
    valid_data = Tokenizer().parse(valid_nl_path, valid_code_path)

    with open(fasttext_corpus_path, 'w') as f:
        for item in train_data:
            f.write(' '.join(item[0]) + '\n')
            f.write(' '.join(item[1]) + '\n')
    word_sim = WordSim(core_term_path, fasttext_corpus_path)

    CodeSearchDataset.create_dataset(train_data, word_sim, train_db_path)
    CodeSearchDataset.create_dataset(valid_data, word_sim, valid_db_path)
