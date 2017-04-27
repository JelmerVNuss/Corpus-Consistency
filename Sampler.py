import random

class Sampler:
    def __init__(self, sampleSize, sampleLength=0, sampleLengthPercentage=0.0):
        self.sampleSize = sampleSize
        self.sampleLength = sampleLength
        self.sampleLengthPercentage = sampleLengthPercentage

    def sample(self, text, usePercentage=False):
        """Randomly sample [sampleSize] pieces of text of length [sampleLength]
        (in characters including whitespace).
        Each sample might overlap with other samples.
        Return a list of samples.
        """
        samples = []

        textLength = len(text)

        if usePercentage:
            sampleLength = int(textLength * self.sampleLengthPercentage)
        else:
            sampleLength = self.sampleLength

        for _ in range(self.sampleSize):
            randomIndexUpperBound = textLength - sampleLength
            startIndex = random.randrange(0, randomIndexUpperBound)
            endIndex = startIndex + sampleLength
            sample = text[startIndex:endIndex]
            samples.append(sample)

        return samples
