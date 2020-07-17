import numpy as np
import matplotlib.pyplot as plt


"""
https://matplotlib.org/gallery/lines_bars_and_markers/errorbar_limits_simple.html#sphx-glr-gallery-lines-bars-and-markers-errorbar-limits-simple-py
"""


def error_bar_1():
    fig = plt.figure()
    x = np.arange(10)
    y = 2.5 * np.sin(x / 20 * np.pi)
    yerr = np.linspace(0.05, 0.2, 10)

    plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')

    plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')

    plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True,
                 label='uplims=True, lolims=True')

    upper_limits = [True, False] * 5
    lower_limits = [False, True] * 5
    plt.errorbar(x, y, yerr=yerr, uplims=upper_limits, lolims=lower_limits,
                 label='subsets of up lims and lolims')

    plt.legend(loc='lower right')
    plt.show()


if __name__ == '__main__':
    error_bar_1()
