import re


class Tokenizer:

    def parse(self, nl_path, code_path):
        return self.__combine(self.__parse_file(nl_path), self.__parse_file(code_path))

    @staticmethod
    def __combine(nl_dict, code_dict):
        ret = []
        for key in nl_dict.keys():
            ret.append((nl_dict[key], code_dict[key]))
        return ret

    def __parse_file(self, file_path):
        ret = {}
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if len(line) > 0:
                    p = line.index('\t')
                    idx = line[: p]
                    tokens = self.__get_tokens(line[p + 1:])
                    ret[idx] = tokens
        return ret

    def __get_tokens(self, content):
        words = [word for word in re.split('[^A-Za-z]+', content) if len(word) > 0]
        ret = []
        for word in words:
            ret += self.__camel_case_split(word)
        return ret

    @staticmethod
    def __camel_case_split(word):
        matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', word)
        return [m.group(0).lower() for m in matches]
