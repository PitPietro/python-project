# It takes as parameter the function to plot
# The given function can be a subclass of NumPy's ufunc
import numpy as np

from math_study.analysis.function_plotting.function_plotter import FunctionPlotter


class UFuncFunctionPlotter(FunctionPlotter):

    def __init__(self, f: np.ufunc, start, end, number, numpy_type=None):
        super().__init__(f, start, end, number, numpy_type)
        self.f = f
        self.start = start
        self.end = end
        self.number = number  # number of elements from start to end
        self.f_x = np.linspace(start, end, number, dtype=numpy_type)
        self.f_y = []

    def fill_y_axis(self):
        for i in range(self.f_x.size):
            self.f_y.append(self.f(self.f_x[i]))

        print('y: ' + str(self.f_y))

        # for i in self.f_x:
        #     self.f_y.append(self.f(i))
