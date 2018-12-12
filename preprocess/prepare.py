import os

import re

from preprocess.lex.token import Tokenizer
from preprocess.lex.word_sim import WordSim
from preprocess.dataset import CodeSearchDataset


def prepare(conf, code_path, nl_path, output_db_path, train_mode=True, train_db_path=None):

    if not train_mode:
        train_corpus_path = os.path.join(conf['data']['wkdir'], re.sub(r'\.db$', '.txt', train_db_path))

    core_term_path = os.path.join(conf['data']['wkdir'], 'conf/core_terms.txt')
    fasttext_corpus_path = os.path.join(conf['data']['wkdir'], re.sub(r'\.db$', '.txt', output_db_path))

    data = Tokenizer().parse(nl_path, code_path)

    train_corpus_content = []
    if not train_mode:
        with open(train_corpus_path, 'r') as f:
            train_corpus_content = f.readlines()
    with open(fasttext_corpus_path, 'w') as f:
        f.writelines(train_corpus_content)
        f.write('\n')
        for item in data:
            f.write(' '.join(item[0]) + '\n')
            f.write(' '.join(item[1]) + '\n')
    word_sim = WordSim(core_term_path, pretrain=(conf['model']['pretrained_wordvec'] == str(True)), update=True, fasttext_corpus_path=fasttext_corpus_path)

    if train_mode:
        CodeSearchDataset.create_dataset(data, word_sim, output_db_path,
                                         int(conf['data']['query_max_len']),
                                         int(conf['data']['code_max_len']),
                                         int(conf['train']['neg_top_k']),
                                         int(conf['train']['neg_sample_size']))
    else:
        CodeSearchDataset.create_dataset(data, word_sim, output_db_path,
                                         int(conf['data']['query_max_len']),
                                         int(conf['data']['code_max_len']),
                                         int(conf['train']['valid_neg_sample_size']),
                                         int(conf['train']['valid_neg_sample_size']))
