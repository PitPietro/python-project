import math

import matplotlib.pyplot as plt
import numpy as np

from math_study.analysis.function_plotting.basic_function import BasicFunction
from math_study.analysis.function_plotting.basic_function_plotter import BasicFunctionPlotter

if __name__ == '__main__':
    # init config
    x_limit = math.pi * 2
    c = 2

    f_x = BasicFunction(2, 1, -2)

    # domain and co-domain settings
    x = np.linspace(-x_limit, x_limit, 1000)

    plt.figure(1)

    plt.plot(x, f_x.value_in_x(x + c), 'g--')
    plt.plot(x, f_x.value_in_x(x))
    plt.plot(x, f_x.value_in_x(x - c), 'y--')

    # get/set the x limits of the current axes
    plt.xlim(-math.pi, math.pi)

    # get/set the y limits of the current axes
    plt.ylim(-math.pi, math.pi)

    # add a horizontal line across the axis
    plt.axhline(y=0, color='k')

    # add a vertical line across the axes
    plt.axvline(x=0, color='k')

    plt.title('Translation on x axis', size=14)

    # save plot to file
    # after plt.show() is called, a new blank figure is created.
    # to avoid paving black images, just save the image before showing it
    plt.savefig('x_translation.svg')

    # display all open figures
    plt.show()

# https://pythonspot.com/matplotlib-save-figure-to-image-file/
