import re

from gensim.parsing import PorterStemmer
from gensim.parsing.preprocessing import remove_stopwords


class Tokenizer:

    def __init__(self):
        self.p = PorterStemmer()

    def parse(self, nl_path, code_path):
        return self.__combine(self.__parse_file(nl_path, True, True), self.__parse_file(code_path, False, True))

    @staticmethod
    def __combine(nl_dict, code_dict):
        ret = []
        for key in sorted([int(key) for key in nl_dict.keys()]):
            ret.append((nl_dict[str(key)], code_dict[str(key)], str(key)))
        return ret

    def __parse_file(self, file_path, rm_stopwords=False, stem=False):
        ret = {}
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if len(line) > 0:
                    p = line.index('\t')
                    idx = line[: p]
                    tokens = self.__get_tokens(line[p + 1:], rm_stopwords, stem)
                    ret[idx] = tokens
        return ret

    def __get_tokens(self, content, rm_stopwords=False, stem=False):
        words = [word for word in re.split('[^A-Za-z]+', content) if len(word) > 0]
        ret = []
        for word in words:
            ret += self.__camel_case_split(word)
        tmp = []
        for word in ret:
            if rm_stopwords:
                word = remove_stopwords(word)
            if len(word) > 0:
                if stem:
                    word = self.p.stem(word)
                tmp.append(word)
        ret = tmp
        return ret

    @staticmethod
    def __camel_case_split(word):
        matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', word)
        return [m.group(0).lower() for m in matches]
