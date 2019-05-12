import nlpnet

tagger = nlpnet.POSTagger('/home/jessica/Documentos/UFSCar/Pesquisa/Projeto/sense2vec-master/pos-pt', language='pt')
print(tagger.tag('o que chama a atenção dos adultos pode chamar atenção das crianças também .'))