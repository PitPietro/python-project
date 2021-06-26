import math
import numpy as np
from math_study.analysis.function_plotting.ufunc_function_plotter import UFuncFunctionPlotter
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def multiple_plotting():
    x_limit = math.pi
    y_limit = 1.5
    rows = 2
    cols = 3

    x = np.linspace(-x_limit, x_limit, 100)

    # functions
    ys = [np.sin(x), np.cos(x), np.tan(x), np.arcsin(x), np.arccos(x), np.arctan(x)]
    y11 = np.sin(x)
    y12 = np.cos(x)
    y13 = np.tan(x)
    y21 = np.arcsin(x)
    y22 = np.arccos(x)
    y23 = np.arctan(x)

    fig, axs = plt.subplots(nrows=rows, ncols=cols, figsize=(10, 5))

    fig.suptitle('Trigonometric functions')
    # axs[0, 0].set_title('sin(x)')
    axs[0, 0].set_xlim(-x_limit, x_limit)
    axs[0, 0].set_ylim(-y_limit, y_limit)

    counter = 0
    for i in range(rows):
        for j in range(cols):
            # print("({}; {})".format(i, j))
            axs[i, j].set_xlim(-x_limit, x_limit)
            axs[i, j].set_ylim(-y_limit, y_limit)
            axs[i, j].plot(x, ys[counter])
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
