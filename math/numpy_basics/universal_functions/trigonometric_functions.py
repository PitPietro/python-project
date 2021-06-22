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


def np_sin(array):
    return np.sin(array)


def np_cos(array):
    return np.cos(array)


def np_tan(array):
    return np.tan(array)


if __name__ == '__main__':
    numpy_test_array = np.arange(10)
    trigonometry_array = _fill_trigonometry_array()

    # trigonometry arrays
    sin_array = np_sin(trigonometry_array)
    cos_array = np_cos(trigonometry_array)
    tan_array = np_tan(trigonometry_array)

    # print out to the user
    print('Numpy Array - Universal Functions - Trigonometric\n')
    print('-------\nTrigonometry:\n')
    print('sin:\n' + str(sin_array))
    print('cos:\n' + str(cos_array))
    print('tan:\n' + str(tan_array))

    # plotting

# https://numpy.org/doc/stable/reference/ufuncs.html
# https://numpy.org/doc/stable/reference/ufuncs.html#trigonometric-functions
