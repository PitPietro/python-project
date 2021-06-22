import matplotlib.pyplot as plt
import numpy as np

from basic_function import BasicFunction
from function_plotter import FunctionPlotter


class BasicFunctionPlotter(FunctionPlotter):

    def __init__(self, f: BasicFunction, start, end, number, numpy_type=None):
        super().__init__(f, start, end, number, numpy_type)
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


if __name__ == '__main__':
    function = BasicFunction(1, 3, 5)
    plotter = BasicFunctionPlotter(function, -50, 50, 500)
    plotter.fill_y_axis()
    plotter.plotting(y_bottom=-1, y_top=40)
