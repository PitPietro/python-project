import math

import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

if __name__ == '__main__':
    # init config
    x_limit = math.pi * 2
    rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
    # for 'Palatino' and other serif fonts use:
    # rc('font',**{'family':'serif','serif':['Palatino']})
    rc('text', usetex=True)

    # domain and co-domain settings
    x = np.linspace(-x_limit, x_limit, 100)
    f_x = np.sin(x)

    c = 2

    # upper function
    g_x = f_x + c

    # lower function
    h_x = f_x - c

    plt.figure(1)

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

    # *math_fontfamily* can be used in most places where there is text,
    # like in the title:
    plt.title(r"$f(x)\pm c$", size=14)  # , **code_font

    # display all open figures
    plt.show()

    # print(matplotlib.font_manager.fontManager.ttflist)

# https://stackoverflow.com/questions/21321670/how-to-change-fonts-in-matplotlib-python#21323217
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
# https://python.astrotech.io/matplotlib/multiple-figures.html#multiple-plots-on-one-figure
