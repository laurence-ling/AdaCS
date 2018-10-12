from __future__ import absolute_import

import os
import argparse
import configparser
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(message)s")

from learning.model import HybridModule
from learning.codesearcher import CodeSearcher
from preprocess.prepare import prepare


def parse_args():
    parser = argparse.ArgumentParser("train and test code search model")
    parser.add_argument("--mode", choices=["train", "eval"], default="train",
                        help="The mode to run. The `train` mode trains a model;"
                        "the `eval` mode evaluates the model.")
    parser.add_argument("-v", "--verbose", default=True, help="Print verbose info.")
    parser.add_argument("-p", "--prepare", action="store_true", default=False, help="Prepare dataset first.")
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
        prepare()
    if option.mode == 'train':
        logger.info("start training model...")
        searcher.train()


if __name__ == '__main__':
    main()
