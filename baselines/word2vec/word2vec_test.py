import gensim
from gensim.models import KeyedVectors

#outp = "../notebooks/model/glove/glove_s300.txt"
outp = "/home/jessica/Documentos/UFSCar/Pesquisa/Projeto/portuguese_word_embeddings/clustering/glove.6B.300d.txt"

model = KeyedVectors.load_word2vec_format(outp, unicode_errors="ignore")

#fantástico fantasticamente aparente aparentemente
#gastando gastou melhorando melhorou
#print(model.wv.most_similar(positive=['gastando', 'melhorou'], negative=['melhorando']))
#print(model.wv.most_similar(positive=['mundo']))
print(model.wv.most_similar(positive=['book'], negative=[]))