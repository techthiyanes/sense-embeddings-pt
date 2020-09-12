import nltk
import glob, os
from pathlib import Path

stemmer = nltk.stem.RSLPStemmer()


def stem_doc(sentence):
    final_sentence = ""
    for word in sentence.split():
        final_sentence = final_sentence + ' ' + stemmer.stem(word)
    #print(final_sentence)
    return str(final_sentence + '\n')

input_path = "/home/jessica/Documentos/UFSCar/Pesquisa/Projeto/gitoficial/corpora_tokenized/lxcorpus/"
output_path = "/home/jessica/Documentos/UFSCar/Pesquisa/Projeto/gitoficial/corpora_tokenized/stem/"
os.chdir(input_path)
for filename in glob.iglob('*.txt'):
    print("corpus: ", filename)
    with open(input_path + filename, 'r', encoding='utf8') as texts:
        with open(output_path + filename + '_stem', 'w', encoding='utf8') as f:
            for line in texts:
                new_line = stem_doc(line)
                f.write(new_line)
            f.close()
    texts.close()