import numpy
import os
import pickle
import sqlite3
from torch.utils.data import Dataset
from data_preprocess.lex.doc_sim import BowSimilarity


class CodeSearchDataset(Dataset):

    @staticmethod
    def create_dataset(data, word_sim, db_path, query_max_size=64, top_k=30, sampling_size=5, print_log=True):

        data = [item for item in data if len(item[0]) <= query_max_size]
        core_term_size = len(word_sim.core_terms) + 1

        if os.path.exists(db_path):
            os.remove(db_path)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE conf (query_max_size INT, core_term_size INT)''')
        cursor.execute('''CREATE TABLE samples (id INT PRIMARY KEY, pkl TEXT)''')
        cursor.execute('''INSERT INTO conf VALUES (?,?)''', [query_max_size, core_term_size])
        conn.commit()

        documents = [item[0] for item in data]
        doc_sim = BowSimilarity(documents)
        samples_buffer = []
        for i in range(len(data)):
            if print_log and i % 100 == 0:
                print(i, '/', len(data))
            item = data[i]
            pos_data = MatchingMatrix(item[0], item[1], word_sim, query_max_size)
            neg_idx_list = doc_sim.negative_sampling(i, top_k, sampling_size)
            neg_data_list = [MatchingMatrix(item[0], data[idx][1], word_sim, query_max_size) for idx in neg_idx_list]
            pkl = pickle.dumps(CodeSearchDataSample(pos_data, neg_data_list))
            samples_buffer.append([i, pkl])
            if i > 0 and (i % 1000 == 0 or i + 1 == range(len(data))):
                cursor.executemany('''INSERT INTO samples VALUES (?,?)''', samples_buffer)
                conn.commit()
                samples_buffer.clear()
        conn.close()

    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''SELECT query_max_size, core_term_size FROM conf''')
        self.query_max_size, self.core_term_size = self.cursor.fetchone()
        self.cursor.execute('''SELECT count(*) FROM samples''')
        self.len = self.cursor.fetchone()

    def __del__(self):
        self.conn.close()

    def __len__(self):
        return self.len

    def __getitem__(self, idx):
        self.cursor.execute('''SELECT pkl FROM samples where id = ?''', [idx])
        return pickle.loads(self.cursor.fetchone())


class CodeSearchDataSample:

    def __init__(self, pos_data, neg_data_list):
        self.pos_data = pos_data
        self.neg_data_list = neg_data_list


class MatchingMatrix:

    def __init__(self, document_1, document_2, word_sim, query_max_size):
        self.matrix = self.__matrix(document_1, document_2, word_sim, query_max_size)
        self.core_terms = self.__core_terms(document_2, word_sim)

    @staticmethod
    def __matrix(document_1, document_2, word_sim, query_max_size):
        ret = numpy.zeros([query_max_size, len(document_2)])
        for i in range(len(document_1)):
            for j in range(len(document_2)):
                ret[i][j] = word_sim.sim(document_1[i], document_2[j])
        return ret

    @staticmethod
    def __core_terms(document, word_sim):
        return [(word_sim.core_term_dict[word] if word in word_sim.core_terms else 1) for word in document]
