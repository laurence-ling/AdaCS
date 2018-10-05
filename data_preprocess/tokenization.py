import re, random

def parse(file_path):
    ret = []
    content = ''
    with open(file_path, 'r') as f:
        content = f.read()
    if len(content) > 0:
        for line in content.split('\t0\n'):
            if len(line) > 0:
                p1 = line.index('\t')
                p2 = line.index('\t', p1 + 1)
                p3 = line.index('\t', p2 + 1)
                query = get_tokens(line[p2 + 1: p3])
                code = get_tokens(line[p3 + 1:].replace('\\n', '\n'))
                ret.append((query, code))
    random.shuffle(ret)
    n = len(ret)
    train_data = ret[:int(n*0.6)]
    dev_data = ret[int(n*0.6+1):int(n*0.8)]
    test_data = ret[int(n*0.8+1):]
    return train_data, dev_data, test_data

def get_tokens(str):
    return [word for word in re.split('[^a-z]+', str.lower()) if word != '']