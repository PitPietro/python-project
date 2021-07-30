import numpy as np


def find_hypotenuse(leg1, leg2):
    try:
        return np.hypot(leg1, leg2)
    except ValueError as valueError:
        print(valueError)
        return []


if __name__ == '__main__':
    height = [4, 5, 6, 7, 8, 9]
    base = [1, 2, 3, 4, 5, 6]
    hypotenuse = find_hypotenuse(height, base)

    print('Numpy Array - Universal Functions - Other\n')
    print('-------\nhypot:\n')
    print('height(s):\n' + str(height))
    print('base(s):\n' + str(base))
    print('hypotenuse(s):\n' + str(hypotenuse))

# https://numpy.org/doc/stable/reference/generated/numpy.hypot.html#numpy.hypot
