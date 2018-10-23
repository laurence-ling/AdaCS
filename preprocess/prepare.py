import os
from preprocess.lex.token import Tokenizer
from preprocess.lex.word_sim import WordSim
from preprocess.dataset import CodeSearchDataset

def prepare():
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
