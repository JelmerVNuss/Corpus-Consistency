import argparse

from Corpus import Corpus
from Sampler import Sampler
from WordCounter import WordCounter
from StatisticsPlotter import StatisticsPlotter
from StatisticsPlotter import FunctionType


ROOT_DIRECTORY = "corpus"
# The confidence level as a decimal point value between 0 and 1.
CONFIDENCE = 0.0#0.95
# Sample size is the conventional measure of the amount of samples.
SAMPLE_SIZE = 25
# Sample length is the length of a sample string containing a small piece of text.
SAMPLE_LENGTH = 1000
SAMPLE_LENGTH_PERCENTAGE = 0.001

TO_LOWERCASE = True
FILTERS = ["\n"]


def main(rootDirectory, words, confidenceLevel, functionType):
    corpus = Corpus(rootDirectory, toLowercase=TO_LOWERCASE, filters=FILTERS)
    #sampler = Sampler(SAMPLE_SIZE, sampleLength=SAMPLE_LENGTH)
    sampler = Sampler(SAMPLE_SIZE, sampleLengthPercentage=SAMPLE_LENGTH_PERCENTAGE)

    documentSamples = {}
    for documentTitle in corpus.documents:
        documentSample = sampler.sample(corpus.documents[documentTitle], usePercentage=True)
        documentSamples[documentTitle] = documentSample

    wordCounter = WordCounter(words, SAMPLE_SIZE)
    wordCounter.countOccurrences(documentSamples)

    dataLabels = sorted(list(wordCounter.occurrences.keys()))
    dataSets = []
    for dataLabel in dataLabels:
        #dataSet = wordCounter.occurrences[dataLabel]
        dataSet = wordCounter.occurrencesPerMillionWords[dataLabel]
        dataSets.append(dataSet)

    statisticsPlotter = StatisticsPlotter(dataLabels, dataSets, CONFIDENCE, words)
    statisticsPlotter.plotStatistics(functionType=functionType)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Load a corpus and test its consistency.')
    parser.add_argument('words', type=str, nargs='+',
                       help='the words that are counted in the corpus (single word, or multiple to serve as a topic)')
    parser.add_argument('--path', type=str, default=ROOT_DIRECTORY,
                        help='the path to the corpus (root) directory')
    parser.add_argument('--confidence', type=float, default=CONFIDENCE,
                        help='the statistical confidence level used, as a percentage')
    parser.add_argument('--functionType', type=FunctionType, default=FunctionType.STANDARD_DEVIATION,
                        help='the type of function used in the statistics plot')

    args = parser.parse_args()
    rootDirectory = args.path
    words = args.words
    confidenceLevel = args.confidence
    functionType = args.functionType

    main(rootDirectory, words, confidenceLevel, functionType)
