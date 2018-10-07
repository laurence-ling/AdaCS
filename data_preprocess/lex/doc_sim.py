from gensim import corpora,models,similarities


class BowSimilarity:

    def __init__(self, all_doc_list):
        dictionary = corpora