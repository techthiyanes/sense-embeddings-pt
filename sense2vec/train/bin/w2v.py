import sense2vec
from gensim import utils, matutils
from numpy import ndarray, dot, array, sqrt, newaxis, zeros, float32 as REAL
from six import string_types
from six.moves import xrange

class SenseKeyedVectors():
    """
    Class to contain vectors and vocab for the Word2Vec training class and other w2v methods not directly
    involved in training such as most_similar()
    """
    def __init__(self):
        self.vectors_norm = None
        self.index2word = []
        self.vectors = zeros((0, 128))
        print("init: ", self.vectors)
        self.vocab = {}
        self.vector_size = 128
        self.index2entity = []

    def init_sims(self, replace=False):
        """Precompute L2-normalized vectors.

        Parameters
        ----------
        replace : bool, optional
            If True - forget the original vectors and only keep the normalized ones = saves lots of memory!

        Warnings
        --------
        You **cannot continue training** after doing a replace.
        The model becomes effectively read-only: you can call
        :meth:`~gensim.models.keyedvectors.WordEmbeddingsKeyedVectors.most_similar`,
        :meth:`~gensim.models.keyedvectors.WordEmbeddingsKeyedVectors.similarity`, etc., but not train.

        """
        if getattr(self, 'vectors_norm', None) is None or replace:
            #logger.info("precomputing L2-norms of word weight vectors")
            if replace:
                for i in xrange(self.vectors.shape[0]):
                    self.vectors[i, :] /= sqrt((self.vectors[i, :] ** 2).sum(-1))
                self.vectors_norm = self.vectors
                print("ReplaceTrue: ", self.vectors)
            else:
                self.vectors_norm = (self.vectors / sqrt((self.vectors ** 2).sum(-1))[..., newaxis]).astype(REAL)
                print(">> ", self.vectors)

    def most_similar(self, positive=None, negative=None, topn=10, restrict_vocab=None, indexer=None):
        """Find the top-N most similar words.
        Positive words contribute positively towards the similarity, negative words negatively.

        This method computes cosine similarity between a simple mean of the projection
        weight vectors of the given words and the vectors for each word in the model.
        The method corresponds to the `word-analogy` and `distance` scripts in the original
        word2vec implementation.

        Parameters
        ----------
        positive : list of str, optional
            List of words that contribute positively.
        negative : list of str, optional
            List of words that contribute negatively.
        topn : int, optional
            Number of top-N similar words to return.
        restrict_vocab : int, optional
            Optional integer which limits the range of vectors which
            are searched for most-similar values. For example, restrict_vocab=10000 would
            only check the first 10000 word vectors in the vocabulary order. (This may be
            meaningful if you've sorted the vocabulary by descending frequency.)

        Returns
        -------
        list of (str, float)
            Sequence of (word, similarity).

        """
        if positive is None:
            positive = []
        if negative is None:
            negative = []

        self.init_sims()

        if isinstance(positive, string_types) and not negative:
            # allow calls like most_similar('dog'), as a shorthand for most_similar(['dog'])
            positive = [positive]

        # add weights for each word, if not already present; default to 1.0 for positive and -1.0 for negative words
        positive = [
            (word, 1.0) if isinstance(word, string_types + (ndarray,)) else word
            for word in positive
        ]
        print("positive: ", positive, " / ", ndarray)
        negative = [
            (word, -1.0) if isinstance(word, string_types + (ndarray,)) else word
            for word in negative
        ]
        print("negative: ", negative, " / ", ndarray)

        # compute the weighted average of all words
        all_words, mean = set(), []
        for word, weight in positive + negative:
            if isinstance(word, ndarray):
                mean.append(weight * word)
                print(">> ", (weight * word))
            else:
                #mean.append(weight * self.word_vec(word, use_norm=True))
                print("vector: ", s2v.__getitem__(word)[1].shape)
                print(type(weight))
                print(type(s2v.__getitem__(word)[1]))
                mean.append(weight * s2v.__getitem__(word)[1])
                # print("mean: ", mean)
                print("weight: ", weight)
                if word in self.vocab:
                    all_words.add(self.vocab[word].index)
        if not mean:
            raise ValueError("cannot compute similarity with no input")
        mean = matutils.unitvec(array(mean).mean(axis=0)).astype(REAL)

        if indexer is not None:
            return indexer.most_similar(mean, topn)

        limited = self.vectors_norm if restrict_vocab is None else self.vectors_norm[:restrict_vocab]
        print("limited: ", limited)
        print("mean: ", mean)
        dists = dot(limited, mean)
        if not topn:
            return dists
        best = matutils.argsort(dists, topn=topn + len(all_words), reverse=True)
        # ignore (don't return) words from the input
        result = [(self.index2word[sim], float(dists[sim])) for sim in best if sim not in all_words]
        return result[:topn]

s2v = sense2vec.load('/home/jessica/Documentos/UFSCar/Pesquisa/Projeto/sense2vec-master/bin/models2v')

query1 = u'mundo|NOUN'
#query2 = u'cachorros|NOUN'
#query1 = u'gastando|VERB'
query2 = u'melhorou|VERB'
query3 = u'melhorando|VERB'


freq1, vector1 = s2v[query1]
freq2, vector2 = s2v[query2]

#vector1 = s2v.__getitem__(query1)
print("freq1: ", freq1)

#print(s2v.data.similarity(vector1, vector2))

words, scores = s2v.most_similar(vector1, 10)
#keyedvectors = SenseKeyedVectors()
#print("return: ", keyedvectors.most_similar(positive=[query1, query2], negative=[query3]))

print(list(zip(words, scores)))



