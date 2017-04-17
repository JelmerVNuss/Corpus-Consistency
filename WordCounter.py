class WordCounter:
    def __init__(self, word):
        self.word = word
        self.occurrences = {}

    def countOccurrencesInSample(self, sample):
        occurrences = sample.count(self.word)
        return occurrences

    def countOccurrences(self, documentSamples):
        for documentTitle in documentSamples:
            samples = documentSamples[documentTitle]
            occurrences = []
            for sample in samples:
                occurrenceCount = self.countOccurrencesInSample(sample)
                occurrences.append(occurrenceCount)
            self.occurrences[documentTitle] = occurrences
