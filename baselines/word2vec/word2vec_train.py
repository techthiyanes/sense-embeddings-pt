import os
import gzip
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

def read_input(input_file):
    documents = []
    """This method reads the input file which is in gzip format"""

    print("reading file {0}...this may take a while".format(input_file))
    with gzip.open(input_file, 'rb') as f:
        for i, line in enumerate(f):

            if (i % 10000 == 0):
                print("read {0} reviews".format(i))
            # do some pre-processing and return list of words for each review
            # text
            documents.append(line)
        return documents

sentences = MySentences('/home/jessica/Documentos/UFSCar/Pesquisa/Projeto/sense2vec-master/bin/corpora/corpora/corpora_tokenized')  # a memory-friendly iterator
#documents = read_input('/home/jessica/Documentos/UFSCar/Pesquisa/Projeto/sense2vec-master/bin/corpora/corpora/corpora_tokenized/corpora_tokenized.tar.gz')
print('terminou corpus')
#sg=1: skigram
#sg=0: cbow
model = Word2Vec(sentences, sg=1, size=300, window=5, min_count=10)
print('finish train')
model.init_sims(replace=True)
model.wv.save_word2vec_format('/home/jessica/Documentos/UFSCar/Pesquisa/Projeto/portuguese_word_embeddings/word2vec/word2vec_s300_ptbr_sg.txt', binary=False)
print('finish')