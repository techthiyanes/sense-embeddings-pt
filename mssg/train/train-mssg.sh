#!/bin/sh

if [ ! -e text8 ]; then
  wget https://dl.dropboxusercontent.com/u/39534006/text8.zip
  unzip text8.zip
fi

if [ ! -e CP.hack ]; then
    echo "Run make_cp.sh script first"
    exit
fi

classpath=`cat CP.hack`
wordvec_app="java -Xmx100g -cp ${classpath} WordVec"

${wordvec_app}  --model=MSSG-MaxOut --train=corpora_tokenized.tar.gz --output=vectors-MSSG_PTBR300.gz --sense=3 --learn-top-v=4000 --size=300 --cbow=0 --window=5 --min-count=10  --threads=23  --negative=1 --sample=0.001 --binary=1 --ignore-stopwords=1 --encoding=UTF-8 --save-vocab=PTBR.vocab.gz --rate=0.025 --delta=0.1
