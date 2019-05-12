import gensim
from gensim.models import KeyedVectors

#outp = "../notebooks/model/glove/glove_s300.txt"
outp = "sense2vec_s128.txt"

model = KeyedVectors.load_word2vec_format(outp, unicode_errors="ignore")

#fantástico fantasticamente aparente aparentemente
#gastando gastou melhorando melhorou
#print(model.wv.most_similar(positive=['gastando|VERB', 'melhorou|VERB'], negative=['melhorando|VERB']))
print(model.wv.most_similar(positive=['fantástico|ADJ', 'aparentemente|ADV'], negative=['aparente|ADJ']))