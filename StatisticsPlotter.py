import numpy as np
import matplotlib
import matplotlib.pyplot as plt


class StatisticsPlotter:
    def __init__(self, dataLabels, dataSets, confidence):
        self.dataLabels = dataLabels
        self.dataSets = dataSets
        self.confidence = confidence
        self.means = self.calculateMeans()
        self.standardDeviations = self.calculateStandardDeviations()

    def calculateStatisticalFunction(self, function):
        statistics = []
        for data in self.dataSets:
            statistic = function(data)
            statistics.append(statistic)
        return statistics

    def calculateMeans(self):
        means = self.calculateStatisticalFunction(function=np.mean)
        return means

    def calculateStandardDeviations(self):
        standardDeviations = self.calculateStatisticalFunction(function=np.std)
        return standardDeviations


    def plotStatistics(self):
        fig, ax = plt.subplots()
        fig.canvas.set_window_title('Corpus Consistency at {}% confidence'.format(round(self.confidence * 100)))
        ax.margins(x=0.15, y=0.01)
        ax.set_title('Average occurences per document (with standard deviations)')

        #ax.set_xlabel('Document')
        ax.set_ylabel('Occurrences per million words')

        x = [self.dataLabels.index(dataLabel) for dataLabel in self.dataLabels]
        y = self.means
        ax.errorbar(x, y, yerr=self.standardDeviations)
        ax.set_xticklabels([""] + self.dataLabels, fontsize='small')

        # Restrict the labels to integers only.
        xa = ax.get_xaxis()
        xa.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
        plt.show()
