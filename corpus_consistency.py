from Corpus import Corpus
from Sampler import Sampler
from WordCounter import WordCounter
from StatisticsPlotter import StatisticsPlotter


ROOT_DIRECTORY = "corpus"
# The confidence level as a decimal point value between 0 and 1.
CONFIDENCE = 0.95
# Sample length is the length of a sample string containing a small piece of text.
SAMPLE_LENGTH = 1000
# Sample size is the conventional measure of the amount of samples.
SAMPLE_SIZE = 25

TO_LOWERCASE = True
FILTERS = ["\n"]
WORD = "and"


if __name__ == "__main__":
    corpus = Corpus(ROOT_DIRECTORY, toLowercase=TO_LOWERCASE, filters=FILTERS)
    sampler = Sampler(SAMPLE_LENGTH, SAMPLE_SIZE)

    documentSamples = {}
    for documentTitle in corpus.documents:
        documentSample = sampler.sample(corpus.documents[documentTitle])
        documentSamples[documentTitle] = documentSample

    wordCounter = WordCounter(WORD, SAMPLE_SIZE)
    wordCounter.countOccurrences(documentSamples)

    dataLabels = sorted(list(wordCounter.occurrences.keys()))
    dataSets = []
    for dataLabel in dataLabels:
        #dataSet = wordCounter.occurrences[dataLabel]
        dataSet = wordCounter.occurrencesPerMillionWords[dataLabel]
        dataSets.append(dataSet)

    statisticsPlotter = StatisticsPlotter(dataLabels, dataSets, CONFIDENCE)
    statisticsPlotter.plotStatistics()
