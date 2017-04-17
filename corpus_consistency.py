from Corpus import Corpus
from Sampler import Sampler


ROOT_DIRECTORY = "corpus"
SAMPLE_SIZE = 100
SAMPLE_AMOUNT = 25


if __name__ == "__main__":
    corpus = Corpus(ROOT_DIRECTORY)
    sampler = Sampler(SAMPLE_SIZE, SAMPLE_AMOUNT)

    documentSamples = {}
    for documentTitle in corpus.documents:
        documentSample = sampler.sample(corpus.documents[documentTitle])
        documentSamples[documentTitle] = documentSample
