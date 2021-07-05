import math

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # init config
    x_limit = math.pi * 2
    c = 2

    # domain and co-domain settings
    x = np.linspace(-x_limit, x_limit, 100)
    f_x = x ** 2 + x

    # right function
    g_x = (x - c) ** 2 + (x - c)

    # left function
    h_x = (x + c) ** 2 + (x + c)

    plt.figure(1)

    plt.plot(x, h_x, 'g--')
    plt.plot(x, f_x)
    plt.plot(x, g_x, 'y--')

    # get/set the x limits of the current axes
    plt.xlim(-math.pi, math.pi)

    # get/set the y limits of the current axes
    plt.ylim(-math.pi, math.pi)

    # add a horizontal line across the axis
    plt.axhline(y=0, color='k')

    # add a vertical line across the axes
    plt.axvline(x=0, color='k')

    plt.title('Translation on x axis', size=14)

    # display all open figures
    plt.show()
