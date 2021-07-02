import math
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    x_limit = math.pi * 2

    x = np.linspace(-x_limit, x_limit, 100)
    f_x = np.sin(x)

    c = 2
    g_x = f_x + c
    h_x = f_x - c

    plt.figure(1)  # plt.figure(1, figsize=(10, 5))  # nop

    plt.plot(x, g_x, 'y--')
    plt.plot(x, f_x)
    plt.plot(x, h_x, 'g--')

    # get/set the x limits of the current axes
    plt.xlim(-math.pi, math.pi)

    # get/set the y limits of the current axes
    plt.ylim(-math.pi, math.pi)

    # add a horizontal line across the axis
    plt.axhline(y=0, color='k')

    # add a vertical line across the axes
    plt.axvline(x=0, color='k')

    # display all open figures
    plt.show()

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
# https://python.astrotech.io/matplotlib/multiple-figures.html#multiple-plots-on-one-figure
