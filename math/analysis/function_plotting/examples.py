import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from scipy import misc
from scipy import optimize


def f(x):
    """
    x ** n means x^n
    2 * x means 2x

    Parameters
    ----------
    x

    Returns
    -------

    """
    return x ** 2


if __name__ == '__main__':
    f_x = np.linspace(-20, 20, 500)
    f_y = []
    
    for i in f_x:
        f_y.append(f(i))

    plt.figure(1)
    plt.plot(f_x, f_y)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.show()

# https://www.webpages.uidaho.edu/~mlowry/Teaching/Analysis&Design/build/html/mathematical_analysis.html
