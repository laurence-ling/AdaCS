import numpy


class Document:

    def __init__(self, id, words):
        self.id = id
        self.words = words


class MatchingMatrix:

    def __init__(self, document_1, document_2, word_sim):
        self.matrix = self.__matrix(document_1, document_2, word_sim)
        self.core_terms = self.core_terms(document_2, word_sim)

    @staticmethod
    def __matrix(document_1, document_2, word_sim):
        ret = numpy.zeros([len(document_1.words), len(document_2.words)])
        for i in range(len(document_1.words)):
            for j in range(len(document_2.words)):
                ret[i][j] = word_sim.sim(document_1.words[i], document_2.words[j])
        return ret

    @staticmethod
    def __core_terms(document, word_sim):
        return [(word_sim.core_term_dict[word] if word in word_sim.core_terms else 1) for word in document.words]