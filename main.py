from __future__ import absolute_import

import os
import argparse
import configparser
import logging

from learning.codesearcher import CodeSearcher
from preprocess.prepare import prepare
from preprocess.dataset import CodeSearchDataset

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(message)s")


def parse_args():
    parser = argparse.ArgumentParser("train and test code search model")
    parser.add_argument("-p", "--prepare", action="store_true", default=False, help="Prepare dataset first.")
    parser.add_argument("--mode", choices=["train", "eval"], default="train",
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
    print(config.options('data'))
    return config


def main():
    conf = get_config()
    option = parse_args()
    searcher = CodeSearcher(conf)
    if option.prepare:
        logger.info("preparing dataset...")
        prepare(conf, conf['data']['train_code_path'], conf['data']['train_nl_path'],
                conf['data']['train_db_path'], train_mode=True)
        prepare(conf, conf['data']['valid_code_path'], conf['data']['valid_nl_path'],
                conf['data']['valid_db_path'], train_mode=False)
        prepare(conf, conf['data']['test_code_path'], conf['data']['test_nl_path'],
                conf['data']['test_db_path'], train_mode=False)
    elif option.mode == 'train':
        logger.info("start training model...")
        searcher.train()
    elif option.mode == 'eval':
        num = input('Please input the epoch of the model to be loaded: ')
        searcher.load_model(searcher.model, num)
        print('load model successfully.')
        test_data = CodeSearchDataset(os.path.join(conf['data']['wkdir'], conf['data']['test_db_path']))
        searcher.eval(test_data)


if __name__ == '__main__':
    main()
