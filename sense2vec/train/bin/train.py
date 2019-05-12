w2v_model = Word2Vec(
        size=size,
        window=window,
        min_count=min_count,
        workers=workers,
        sample=1e-5,
        negative=negative,
        iter=epochs
    )

    sentences = PathLineSentences(path)

    print("building the vocabulary...")
    w2v_model.build_vocab(sentences)

    print("training the model...")
    w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=w2v_model.iter)

    print("creating the sense2vec model...")
    vector_map = VectorMap(size)

    for string in w2v_model.wv.vocab:
        vocab = w2v_model.wv.vocab[string]
        freq, idx = vocab.count, vocab.index
        if freq < min_count:
            continue
        vector = w2v_model.wv.vectors[idx]
        vector_map.borrow(string, freq, vector)

    print("saving the model to file...")
    vector_map.save(out_path)