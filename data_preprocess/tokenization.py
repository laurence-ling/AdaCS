import re, random

def parse(train_nl_path, valid_nl_path, test_nl_path, train_code_path, valid_code_path, test_code_path, print_log = True):
    
    train_data = combine(parse_file(train_nl_path), parse_file(train_code_path))
    valid_data = combine(parse_file(valid_nl_path), parse_file(valid_code_path))
    test_data = combine(parse_file(test_nl_path), parse_file(test_code_path))

    if print_log:
        query_max_len = 0
        code_max_len = 0
        for item in train_data + valid_data + test_data:
            if len(item[0]) > query_max_len: query_max_len = len(item[0])
            if len(item[1]) > code_max_len: code_max_len = len(item[1])
        print('TrainData size = ', len(train_data))
        print('ValidData size = ', len(valid_data))
        print('TestData size = ', len(test_data))
        print('Max query length = ', query_max_len)
        print('Max code length = ', code_max_len)

    return train_data, valid_data, test_data

def combine(nl_dict, code_dict):
    ret = []
    for key in nl_dict.keys():
        ret.append((nl_dict[key], code_dict[key]))
    return ret

def parse_file(file_path):
    ret = {}
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if len(line) > 0:
                p = line.index('\t')
                idx = line[: p]
                tokens = get_tokens(line[p+1:])
                ret[idx] = tokens
    return ret

def get_tokens(str):
    words = [word for word in re.split('[^A-Za-z]+', str) if word != '']
    ret = []
    for word in words:
        ret += camel_case_split(word)
    ret = [word for word in ret if len(word) > 1]
    return ret

def camel_case_split(word):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', word)
    return [m.group(0).lower() for m in matches]