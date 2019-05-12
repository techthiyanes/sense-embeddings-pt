import sense2vec
import re

array = ""
#s2v = sense2vec.load('/home/jessica/Documentos/UFSCar/Pesquisa/Projeto/sense2vec-master/bin/models2v')
s2v = sense2vec.load('/home/jessica/Documentos/UFSCar/Pesquisa/Projeto/sense2vec-master/bin/models2v11-05')
items = s2v.items()
with open('sense2vec_s300_ptbreu_sg.txt', 'w', encoding='utf-8') as f:
    f.write("479059 " + "300\n")
    for i, item in enumerate(items):
        key = item[0]
        if key != '':
            array = str(s2v.__getitem__(key)[1])
            array = array.replace('[', '')
            array = array.replace(']', '')
            array = array.strip()
            array = re.sub(' +', ' ', array)
            array = array.replace('\n', '')
            line = key.strip() + ' ' + array + '\n'
            print(i)
            f.write(line)
    f.close()

#Ativa venv
# python convertbintotext.py

