import spacy
from sense2vec import Sense2VecComponent

nlp = spacy.load('en')
s2v = Sense2VecComponent('/path/to/reddit_vectors-1.1.0')
nlp.add_pipe(s2v)

doc = nlp(u"A sentence about natural language processing.")
assert doc[3].text == u'natural language processing'
freq = doc[3]._.s2v_freq
vector = doc[3]._.s2v_vec
most_similar = doc[3]._.s2v_most_similar(3)
# [(('natural language processing', 'NOUN'), 1.0),
#  (('machine learning', 'NOUN'), 0.8986966609954834),
#  (('computer vision', 'NOUN'), 0.8636297583580017)]