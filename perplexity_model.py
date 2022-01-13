import nltk
from nltk.lm import MLE, preprocessing
from typing import List


def tokenize_text_sentences_and_words(corpus: str) -> List[List[str]]:
    sentences = nltk.sent_tokenize(corpus.lower())
    return [nltk.word_tokenize(sentence) for sentence in sentences]


def train_perplexity_model(corpus: str):
    tk_corpus = tokenize_text_sentences_and_words(corpus)
    train, vocab = preprocessing.padded_everygram_pipeline(2, tk_corpus)
    lm = MLE(2)
    lm.fit(train, vocab)
    return lm
