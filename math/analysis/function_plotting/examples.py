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


if __name__ == '__main__':
    main_f_x = np.linspace(-20, 20, 500)
    main_f_y = []

    for i in main_f_x:
        main_f_y.append(f(i, 0.5, 2, 5))

    plt.figure(1)
    plt.plot(main_f_x, main_f_y)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.show()

    fill_ordinate_axis(-4, 4, 8)

# https://www.webpages.uidaho.edu/~mlowry/Teaching/Analysis&Design/build/html/mathematical_analysis.html
