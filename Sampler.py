import random

class Sampler():
    def __init__(self, sampleLength, sampleSize):
        self.sampleLength = sampleLength
        self.sampleSize = sampleSize

    def sample(self, text):
        """Randomly sample [sampleSize] pieces of text of length [sampleLength]
        (in characters including whitespace).
        Each sample might overlap with other samples.
        Return a list of samples.
        """
        samples = []

        for _ in range(self.sampleSize):
            randomIndexUpperBound = len(text) - self.sampleLength
            startIndex = random.randrange(0, randomIndexUpperBound)
            endIndex = startIndex + self.sampleLength
            sample = text[startIndex:endIndex]
            samples.append(sample)

        return samples
