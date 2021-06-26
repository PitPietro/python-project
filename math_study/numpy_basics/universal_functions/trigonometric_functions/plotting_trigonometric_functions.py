import math
import numpy as np
from math_study.analysis.function_plotting.ufunc_function_plotter import UFuncFunctionPlotter
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def multiple_plotting():
    x = np.linspace(-math.pi, math.pi, 100)
    y11 = np.sin(x)
    y12 = np.cos(x)
    y13 = np.tan(x)
    y21 = np.arcsin(x)
    y22 = np.arccos(x)
    y23 = np.arctan(x)

    fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(10, 5))

    fig.suptitle('Trigonometric functions')
    axs[0, 0].set_title('sin(x)')
    axs[0, 0].set_xlim(-math.pi, math.pi)
    axs[0, 0].set_ylim(-1.5, 1.5)

    axs[0, 0].plot(x, y11)
    axs[0, 1].plot(x, y12)
    axs[0, 2].plot(x, y13)
    axs[1, 0].plot(x, y21)
    axs[1, 1].plot(x, y22)
    axs[1, 2].plot(x, y23)

    # display all open figures
    plt.show()

    print('axes object: ' + str(axs[0, 0]))


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
