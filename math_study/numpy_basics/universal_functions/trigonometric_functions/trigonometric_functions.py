# In NumPy, universal functions are instances of the numpy.ufunc class.
# NumPy provides mathematical functions (such as sin, exp, log, ...), which are called "universal functions"(ufunc).
# Within NumPy, these functions operate elementwise on an array, producing an array as output.
# All trigonometric functions use radians when an angle is called for.
import math
import numpy as np


def _fill_trigonometry_array():
    """
    Utility function to fill the trigonometry array
    Returns
    -------
    The array filled with useful angle measures
    """
    trig_array = [
        0,  # 0°
        math.pi / 6,  # 30°
        math.pi / 4,  # 45°
        math.pi / 3,  # 60°
        math.pi / 2,  # 90°
        (2 * math.pi) / 3,  # 120°
        (3 * math.pi) / 4,  # 135°
        (5 * math.pi) / 6,  # 150°
        math.pi,  # 180°
        (7 * math.pi) / 6,  # 210°
        (5 * math.pi) / 4,  # 225°
        (4 * math.pi) / 3,  # 240°
        (3 * math.pi) / 2,  # 270°
        (5 * math.pi) / 3,  # 300°
        (7 * math.pi) / 4,  # 315°
        (11 * math.pi) / 6,  # 330°
    ]
    return trig_array


def _fill_arc_trigonometry_array():
    """
    Utility function to fill the trigonometry array used by some arc* functions (arcsin, arccos, ...)
    Returns
    -------
    The array filled with useful angle measures
    """
    arc_trig_array = [
        -1,
        math.pi / 4,  # -45°
        math.pi / 6,  # -30°
        0,  # 0°
        math.pi / 6,  # 30°
        math.pi / 4,  # 45°
        1
    ]
    return arc_trig_array


def np_sin(array):
    return np.sin(array)


def np_cos(array):
    return np.cos(array)


def np_tan(array):
    return np.tan(array)


def np_arcsin(array):
    return np.arcsin(array)


def np_arccos(array):
    return np.arccos(array)


def np_arctan(array):
    return np.arctan(array)


if __name__ == '__main__':
    trigonometry_array = _fill_trigonometry_array()
    arc_trigonometry_array = _fill_arc_trigonometry_array()

    # trigonometry arrays
    sin_array = np_sin(trigonometry_array)
    cos_array = np_cos(trigonometry_array)
    tan_array = np_tan(trigonometry_array)

    arcsin_array = np_arcsin(arc_trigonometry_array)
    arccos_array = np_arccos(arc_trigonometry_array)
    arctan_array = np_arctan(trigonometry_array)

    # print out to the user
    print('Numpy Array - Universal Functions - Trigonometric\n')
    print('-------\nTrigonometry:\n')
    print('sin:\n' + str(sin_array))
    print('cos:\n' + str(cos_array))
    print('tan:\n' + str(tan_array))
    print('---')
    print('arcsin:\n' + str(arcsin_array))
    print('arccos:\n' + str(arccos_array))
    print('arctan:\n' + str(arctan_array))

    # # plotting cos
    # numpy_test_array = np.arange(10)
    # f_x = np.linspace(-math.pi, math.pi, 100)
    # f_y = np.zeros((1, 100))
    #
    # for i in range(f_x.size):
    #     f_y[0][i] = np.cos(f_x[i])
    #
    # plt.figure(1)
    # plt.plot(f_x, f_y[0])
    # plt.xlim(-math.pi, math.pi)
    # plt.ylim(-1.5, 1.5)
    #
    # # Add a horizontal line across the axis.
    # plt.axhline(y=0, color='k')
    #
    # # Add a vertical line across the axes.
    # plt.axvline(x=0, color='k')
    # plt.show()

# https://realpython.com/python-import/ (import issue)
# https://numpy.org/doc/stable/reference/ufuncs.html
# https://numpy.org/doc/stable/reference/ufuncs.html#trigonometric-functions
