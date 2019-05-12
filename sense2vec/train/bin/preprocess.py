#!/usr/bin/env python
# coding: utf-8
"""This script can be used to preprocess a corpus for training a sense2vec
model. It take text file with one sentence per line, and outputs a text file
with one sentence per line in the expected sense2vec format (merged noun
phrases, concatenated phrases with underscores and added "senses").

Example input:
Rats, mould and broken furniture: the scandal of the UK's refugee housing

Example output:
Rats|NOUN ,|PUNCT mould|NOUN and|CCONJ broken_furniture|NOUN :|PUNCT
the|DET scandal|NOUN of|ADP the|DET UK|GPE 's|PART refugee_housing|NOUN

DISCLAIMER: The sense2vec training and preprocessing tools are still a work in
progress. Please note that this script hasn't been optimised for efficiency yet
and doesn't paralellize or batch up any of the work, so you might have to
add this functionality yourself for now.
"""
from __future__ import print_function, unicode_literals

#import sense2vec
#from sense2vec import transform_doc
import spacy
import nlpnet
from pathlib import Path
from tqdm import tqdm
import re
import plac
import glob, os


def transform_doc(doc):
    """
    Transform a spaCy Doc to match the sense2vec format: merge entities
    into one token and merge noun chunks without determiners.
    """
    #if not doc.is_tagged:
    #    raise ValueError("Can't run sense2vec: document not tagged.")
    #print("doc: ", doc)
    for ent in doc.ents:
        #print("Entidades: ", ent)
        ent.merge(tag=ent.root.tag_, lemma=ent.root.lemma_,
                  ent_type=ent.label_)

    #for np in doc.noun_chunks:
    #for np in doc:
        #if (np.pos_ == 'NOUN'):
            #print("Subs: ", np)
            #print("dep: ", np.dep_)
            #while len(np) > 1 and np.dep_ not in ('advmod', 'amod', 'compound'):
                #np = np[1:]
            #np.merge(tag=np.root.tag_, lemma=np.root.lemma_,
                    #ent_type=np.root.ent_type_)
    return doc


def represent_word(word):
    if word.like_url:
        return '%%URL|X'
    text = re.sub(r'\s', '_', word.text)
    tag = word.ent_type_ or word.pos_ or '?'
    return text + '|' + tag


def represent_word_dataset(word):
    text = re.sub(r'\s', '_', word.text)
    tag = word.ent_type_ or word.pos_ or '?'
    return str(text) + '|' + str(tag)


def represent_word_nlpnet(word, tagger):
    tag = tagger.tag(str(word))[0][0][1]
    #print('word: ', word + '|' + tag)
    return str(word) + '|' + tag

def represent_sentence_nlpnet(sent, tagger):
    tags = tagger.tag(str(sent))
    sent_tagged = ""
    for tag in tags[0]:
        word = str(tag).replace("(", "")
        word = word.replace(")", "")
        word = word.replace("\', ", "|")
        word = word.replace("\'", "")
        sent_tagged = sent_tagged + ' ' + word
    return sent_tagged


def represent_doc(doc):
    tagger = nlpnet.POSTagger('/home/jessica/Documentos/UFSCar/Pesquisa/Projeto/sense2vec-master/pos-pt', language='pt')
    strings = []
    for sent in doc.sents:
        if sent.text.strip():
            sentence = represent_sentence_nlpnet(sent, tagger)
            strings.append(sentence)
    return '\n'.join(strings) + '\n' if strings else ''


def represent_dataset(doc):
    strings = []
    nlp = spacy.load('pt_core_news_sm')
    for sent in doc:
        #print("sent: ", sent)
        if sent[0] == ':':
            #sent = sent.replace('\n', '')
            #print(sent.strip())
            strings.append(sent.strip())
        else:
            if sent.strip():
                doc = nlp(sent)
                words = ' '.join(represent_word_dataset(w) for w in doc if not w.is_space)
                #print('words: ', words)
                strings.append(words)
    return '\n'.join(strings) + '\n' if strings else ''


@plac.annotations(
    in_file=("Path to input file", "positional", None, str),
    out_file=("Path to output file", "positional", None, str),
    spacy_model=("Name of spaCy model to use", "positional", None, str),
    n_workers=("Number of workers", "option", "n", int))
def main(in_file, out_file, spacy_model='pt_core_news_sm', n_workers=4): #en_core_web_sm
    input_path = Path(in_file)
    output_path = Path(out_file)
    if not input_path.exists():
        raise IOError("Can't find input file: {}".format(input_path))
    nlp = spacy.load(spacy_model)
    print("Using spaCy model {}".format(spacy_model))
    #nlp.add_pipe(transform_doc, name='sense2vec')
    lines_count = 0

    os.chdir("corpora/corpora/teste")
    #os.chdir("analogies")
    for filename in glob.iglob('*.txt'):
        print("corpus: ", filename)
        input_path = Path(filename)
        with input_path.open('r', encoding='utf8') as texts:
            #lines = texts.readlines()
            docs = nlp.pipe(texts, n_threads=n_workers)
            lines_pos = (represent_doc(doc) for doc in docs)
            #lines_pos = represent_dataset(lines)
            output_path = Path("../corpora_pos_nlpnet/" + filename + "_pos")
            with output_path.open('w', encoding='utf8') as f:
                #print(lines)
                for line in tqdm(lines_pos, desc='Lines', unit=''):
                    lines_count += 1
                    f.write(line)
                #os.remove(filename)
    print("Successfully preprocessed {} lines".format(lines_count))
    print("{}".format(output_path.resolve()))


if __name__ == '__main__':
    plac.call(main)

#nohup python3 preprocess.py input.txt output.txt &> nohup2.out&
