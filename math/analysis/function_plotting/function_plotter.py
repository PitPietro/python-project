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
        self.zeros = np.zeros((2, number), dtype=numpy_type)
        print('zeros: ' + str(self.zeros))

    def fill_y_axis(self):
        print("x values:\n" + str(self.f_x))
        print("y value:\n" + str(self.f_y))

        for i in self.f_x:
            print(i)
            self.f_y.append(self.f.value_in_x(i))
        print("y value:\n" + str(self.f_y))

    def plotting(self, x_left=-10., y_bottom=-10, x_right=10, y_top=10):
        # create a new figure or activate an existing one
        plt.figure(1)
        plt.plot(self.f_x, self.f_y)

        # get/set the x limits of the current axes
        plt.xlim(x_left, x_right)

        # get/set the y limits of the current axes
        plt.ylim(y_bottom, y_top)

        # add a horizontal line across the axis
        plt.axhline(y=0, color='k')

        # add a vertical line across the axes
        plt.axvline(x=0, color='k')

        # display all open figures
        plt.show()


if __name__ == '__main__':
    function = BasicFunction(1, 3, 5)
    plottingFunction = FunctionPlotter(function, -50, 50, 500)
    plottingFunction.fill_y_axis()
    plottingFunction.plotting(y_bottom=-1, y_top=40)
