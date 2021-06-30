import math
import numpy as np
from math_study.analysis.function_plotting.ufunc_function_plotter import UFuncFunctionPlotter
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


limit = {
    "x_sx": -math.pi,
    "x_dx": math.pi,
    "y_down": -1.5,
    "y_up": 1.5,
}

arccos_limit = {
    "x_sx": -math.pi,
    "x_dx": math.pi,
    "y_down": 0.5,
    "y_up": 2.5,
}


def multiple_plotting():
    x_limit = math.pi
    y_limit = 1.5
    rows = 2
    cols = 3

    limits = [limit, limit, limit, limit, arccos_limit, limit]

    x = np.linspace(-x_limit, x_limit, 100)

    # functions
    ys = [np.sin(x), np.cos(x), np.tan(x), np.arcsin(x), np.arccos(x), np.arctan(x)]
    fig, axs = plt.subplots(nrows=rows, ncols=cols, figsize=(10, 5))

    fig.suptitle('Trigonometric functions')

    counter = 0
    for i in range(rows):
        for j in range(cols):
            # get/set the x limits of the current axes
            axs[i, j].set_xlim(limits[counter].get('x_sx'), limits[counter].get('x_dx'))
            # get/set the y limits of the current axes
            axs[i, j].set_ylim(limits[counter].get('y_down'), limits[counter].get('y_up'))
            axs[i, j].plot(x, ys[counter])
            # add a horizontal line across the axis
            axs[i, j].axhline(y=0, color='k')
            # add a vertical line across the axes
            axs[i, j].axvline(x=0, color='k')

            counter = counter + 1

    # display all open figures
    plt.show()


if __name__ == '__main__':
    multiple_plotting()

    # x = np.linspace(0, 2, 100)
    #
    # ax = plt.figure().gca()  # ``gca`` - get current axes
    #
    # ax.plot(x, x, label='linear')
    # ax.plot(x, x ** 2, label='quadratic')
    # ax.plot(x, x ** 3, label='cubic')
    #
    # ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.show()

    # plotting
    # plotter = UFuncFunctionPlotter(np.cos, -math.pi, math.pi, 100)
    # plotter.plotting(-math.pi, math.pi, -1.5, 1.5)
    #
    # plotter = UFuncFunctionPlotter(np.cos, -math.pi, math.pi, 100)
    # plotter.fill_y_axis()
    # plotter.plotting(-math.pi, math.pi, -1.5, 1.5)

# https://python.astrotech.io/matplotlib/multiple-figures.html#multiple-figures-with-single-plots
# https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/subplots_demo.html
