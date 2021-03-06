class WordCounter:
    def __init__(self, words, sampleSize):
        self.words = words
        self.sampleSize = sampleSize
        self.occurrences = {}

    @property
    def occurrencesPerMillionWords(self):
        occurrencesPerMillionWords = {}
        for documentTitle in self.occurrences:
            occurrencesPerMillionWords[documentTitle] = [x / (self.sampleSize * 1000000) for x in self.occurrences[documentTitle]]
        return occurrencesPerMillionWords

    def countOccurrencesInSample(self, sample):
        occurrences = 0
        for word in self.words:
            occurrences += sample.count(word)
        return occurrences

    def countOccurrences(self, documentSamples):
        for documentTitle in documentSamples:
            samples = documentSamples[documentTitle]
            occurrences = []
            for sample in samples:
                occurrenceCount = self.countOccurrencesInSample(sample)
                occurrences.append(occurrenceCount)
            self.occurrences[documentTitle] = occurrences
