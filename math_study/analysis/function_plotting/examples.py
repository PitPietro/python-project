import matplotlib.pyplot as plt
import numpy as np


def f(x, a=0., b=0., c=0.):
    """
    Basic function representation: ax^2 + bx + c
    Parameters
    ----------
    x coordinate on the abscissa axis
    a coefficient of x^2
    b coefficient of x
    c known term

    Returns
    -------
    The function value at the given x coordinate
    """
    return a * x ** 2 + b * x + c


def fill_ordinate_axis(start, end, number, numpy_type=None):
    f_x = np.linspace(start, end, number, dtype=numpy_type)
    f_y = np.zeros((1, number), dtype=numpy_type)
    print("x values:\n" + str(f_x))
    print("y value:\n" + str(f_y))

    for i in range(f_x.size):
        print(i)
        f_y[0][i] = f(f_x[i], 0.5, 2, 5)
    print("y value:\n" + str(f_y))

    plt.figure(1)
    plt.plot(f_x, f_y[0])
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # Add a horizontal line across the axis.
    plt.axhline(y=0, color='k')

    # Add a vertical line across the axes.
    plt.axvline(x=0, color='k')
    plt.show()


if __name__ == '__main__':
    main_f_x = np.linspace(-20, 20, 500)
    main_f_y = []

    for main_i in main_f_x:
        main_f_y.append(f(main_i, 0.5, 2, 5))

    # plt.figure(1)
    # plt.plot(main_f_x, main_f_y)
    # plt.xlim(-10, 10)
    # plt.ylim(-10, 10)
    # plt.show()

    fill_ordinate_axis(-20, 20, 500)

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhline.html
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html
# https://www.webpages.uidaho.edu/~mlowry/Teaching/Analysis&Design/build/html/mathematical_analysis.html
