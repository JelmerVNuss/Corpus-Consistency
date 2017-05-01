import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from enum import Enum


class FunctionType(Enum):
    STANDARD_DEVIATION = "standard_deviation"
    BOX_PLOT = "box_plot"


class StatisticsPlotter:
    def __init__(self, dataLabels, dataSets, confidence, words):
        self.dataLabels = dataLabels
        self.dataSets = dataSets
        self.confidence = confidence
        self.words = words
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


    def plotStatistics(self, functionType=FunctionType.STANDARD_DEVIATION):
        fig, ax = plt.subplots()
        fig.canvas.set_window_title('Corpus Consistency at {}% confidence'.format(round(self.confidence * 100)))
        ax.margins(x=0.05, y=0.01)

        if functionType == FunctionType.STANDARD_DEVIATION:
            self.plotStandardDeviation(fig, ax)
        elif functionType == FunctionType.BOX_PLOT:
            self.plotBoxPlot(fig, ax)
        else:
            raise ValueError("Function type not implemented: {}".format(functionType))

        ax.set_xticklabels([""] + self.dataLabels, fontsize='small', rotation=70)

        # Restrict the labels to integers only.
        xa = ax.get_xaxis()
        xa.set_major_locator(matplotlib.ticker.MultipleLocator(1.0))
        # Set the accuracy of the occurrences per million words to 3 significant digits.
        # That is, up to 1/1000 words per million words can be plotted.
        ax.yaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.9f'))

        # Start the y-axis at 0 words per million.
        ax.set_ylim(ymin=0)

        plt.show()

    def plotStandardDeviation(self, fig, ax):
        ax.set_title('Average occurences of {} per document (with standard deviation)'.format(self.words))

        x = [self.dataLabels.index(dataLabel) for dataLabel in self.dataLabels]
        y = clamp(self.means)
        ax.errorbar(x, y, yerr=clamp(self.standardDeviations))

    def plotBoxPlot(self, fig, ax):
        ax.set_title('Box plot of occurences of {} per document'.format(self.words))
        ax.boxplot(self.dataSets)


def clamp(integerList):
    integerList = [max(0, x) for x in integerList]
    return integerList
