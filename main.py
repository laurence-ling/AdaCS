from __future__ import absolute_import

import os
import argparse
import configparser
import logging

import re

import torch

from learning.codesearcher import CodeSearcher
from preprocess.lex.token import Tokenizer
from preprocess.lex.word_sim import WordSim
from preprocess.prepare import prepare
from preprocess.dataset import CodeSearchDataset, MatchingMatrix

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(message)s")


def parse_args():
    parser = argparse.ArgumentParser("train and test code search model")
    parser.add_argument("-p", "--prepare", action="store_true", default=False, help="Prepare dataset first.")
    parser.add_argument("--mode", choices=["train", "eval", "debug"], default="train",
                        help="The mode to run. The `train` mode trains a model;"
                        "the `eval` mode evaluates the model.")
    parser.add_argument("-v", "--verbose", default=True, help="Print verbose info.")
    option = parser.parse_args()
    return option

def get_config():
    basedir = os.path.dirname(__file__)
    config = configparser.ConfigParser()
    config.read(os.path.join(basedir, './conf/config.ini'))
    config.set('data', 'wkdir', basedir)
    return config


def main():
    conf = get_config()
    option = parse_args()
    if option.prepare:
        logger.info("preparing dataset...")
        prepare(conf, conf['data']['train_code_path'], conf['data']['train_nl_path'], conf['data']['train_db_path'], train_mode=True)
        prepare(conf, conf['data']['valid_code_path'], conf['data']['valid_nl_path'], conf['data']['valid_db_path'], train_mode=False, train_db_path=conf['data']['train_db_path'])
        prepare(conf, conf['data']['test_code_path'], conf['data']['test_nl_path'], conf['data']['test_db_path'], train_mode=False, train_db_path=conf['data']['train_db_path'])
    elif option.mode == 'train':
        logger.info("start training model...")
        searcher = CodeSearcher(conf)
        searcher.train()
    elif option.mode == 'eval':
        num = input('Please input the epoch of the model to be loaded: ')
        searcher = CodeSearcher(conf)
        searcher.load_model(int(num))
        print('load model successfully.')
        searcher.eval2()
    elif option.mode == 'debug':
        line = input('Please input two item ids, seperated by space: ')
        eles = line.strip().split()
        data = Tokenizer().parse(os.path.join(conf['data']['wkdir'], conf['data']['test_nl_path']),
                                 os.path.join(conf['data']['wkdir'], conf['data']['test_code_path']))
        fasttext_corpus_path = os.path.join(conf['data']['wkdir'], re.sub(r'\.db$', '.txt', conf['data']['test_db_path']))
        core_term_path = os.path.join(conf['data']['wkdir'], 'conf/core_terms.txt')
        word_sim = WordSim(core_term_path, pretrain=True, fasttext_corpus_path=fasttext_corpus_path)
        for a in range(len(data)):
            if data[a][2] == eles[0]:
                for b in range(len(data)):
                    if data[b][2] == eles[1]:
                        matrix = MatchingMatrix(data[a][0], data[b][1], data[a][2], word_sim, conf['data']['query_max_len'])
                        for i in range(len(matrix)):
                            for j in range(len(matrix[0])):
                                print('%5.2f' % data.matrix[i][j], end=', ')
                            print()
                        break
                break

if __name__ == '__main__':
    main()
