from Corpus import Corpus
from Sampler import Sampler


ROOT_DIRECTORY = "corpus"
# Sample length is the length of a sample string containing a small piece of text.
SAMPLE_LENGTH = 100
# Sample size is the conventional measure of the amount of samples.
SAMPLE_SIZE = 25


if __name__ == "__main__":
    corpus = Corpus(ROOT_DIRECTORY)
    sampler = Sampler(SAMPLE_LENGTH, SAMPLE_SIZE)

    documentSamples = {}
    for documentTitle in corpus.documents:
        documentSample = sampler.sample(corpus.documents[documentTitle])
        documentSamples[documentTitle] = documentSample
