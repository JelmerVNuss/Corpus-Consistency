import numpy as np
import matplotlib
import matplotlib.pyplot as plt


class StatisticsPlotter:
    def __init__(self, dataLabels, dataSets):
        self.dataLabels = dataLabels
        self.dataSets = dataSets
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
        ax.margins(x=0.05, y=0.01)

        x = [self.dataLabels.index(dataLabel) for dataLabel in self.dataLabels]
        y = self.means
        ax.errorbar(x, y, yerr=self.standardDeviations)
        ax.set_xticklabels(self.dataLabels)

        # Restrict the labels to integers only.
        xa = ax.get_xaxis()
        xa.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
        plt.show()
