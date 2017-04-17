import numpy as np
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
        x = [self.dataLabels.index(dataLabel) for dataLabel in self.dataLabels]
        y = self.means
        ax.errorbar(x, y, yerr=self.standardDeviations)
        plt.show()
