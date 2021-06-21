import matplotlib.pyplot as plt
import numpy as np

from basic_function import BasicFunction


class FunctionPlotter:

    def __init__(self, f: BasicFunction, start, end, number, numpy_type=None):
        self.f = f
        self.start = start
        self.end = end
        self.number = number  # number of elements from start to end
        self.f_x = np.linspace(start, end, number, dtype=numpy_type)
        self.f_y = []

    def fill_y_axis(self):
        print("x values:\n" + str(self.f_x))
        print("y value:\n" + str(self.f_y))

        for i in self.f_x:
            print(i)
            self.f_y.append(self.f.value_in_x(i))
        print("y value:\n" + str(self.f_y))

    def plotting(self):
        plt.figure(1)
        plt.plot(self.f_x, self.f_y)
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)

        # Add a horizontal line across the axis.
        plt.axhline(y=0, color='k')

        # Add a vertical line across the axes.
        plt.axvline(x=0, color='k')
        plt.show()


if __name__ == '__main__':
    function = BasicFunction(2, 3, 5)
    plottingFunction = FunctionPlotter(function, -20, 20, 500)
    plottingFunction.fill_y_axis()
    plottingFunction.plotting()
