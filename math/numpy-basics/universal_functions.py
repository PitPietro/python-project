# NumPy provides mathematical functions (such as sin, cos, and exp), which are called "universal functions"(ufunc).
# Within NumPy, these functions operate elementwise on an array, producing an array as output.
import math

import numpy as np


def _fill_trigonometry_array():
    trig_array = [
        0,  # 0
        math.pi / 6,  # 30°
        math.pi / 4,  # 45°
        math.pi / 3,  # 60°
        math.pi / 2,  # 90°
        (2 * math.pi) / 3,  # 120°
        (3 * math.pi) / 4,  # 135°
        (5 * math.pi) / 6,  # 150°
        math.pi,  # 180°
    ]
    return trig_array


def np_sin(array):
    return np.sin(array)


def np_cos(array):
    return np.cos(array)


if __name__ == '__main__':
    numpy_test_array = np.arange(10)
    trigonometry_array = _fill_trigonometry_array()
    sin_array = np_sin(trigonometry_array)
    cos_array = np_cos(trigonometry_array)

    print('Numpy Array - Universal Functions\n')
    print('-------\nTrigonometry:\n')
    print('sin:\n' + str(sin_array))
    print('cos:\n' + str(cos_array))
