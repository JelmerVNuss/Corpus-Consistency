import random

class Sampler():
    def __init__(self, sampleSize, sampleAmount):
        self.sampleSize = sampleSize
        self.sampleAmount = sampleAmount

    def sample(text):
        """Randomly sample [sampleAmount] pieces of text of length [sampleSize]
        (in characters including whitespace).
        Each sample might overlap with other samples.
        Return a list of samples.
        """
        samples = []

        for _ in range(sampleAmount):
            randomIndexUpperBound = len(text) - sampleSize
            startIndex = random.randrange(0, randomIndexUpperBound)
            endIndex = startIndex + sampleSize
            sample = text[startIndex:endIndex]
            samples.append(sample)

        return samples
