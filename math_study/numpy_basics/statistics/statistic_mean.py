import numpy as np

from math_study.numpy_basics.statistics.statistics import ordered_data

if __name__ == '__main__':
    print('Numpy - Statistic - mean')

    # https://numpy.org/doc/stable/reference/generated/numpy.mean.html
    print('\nCompute the arithmetic mean of the whole array:')
    print(ordered_data.mean())

    print('\nCompute the arithmetic mean along the specified axis:')
    print(ordered_data.mean(axis=0))  # array filled with vertical means
    print(ordered_data.mean(axis=1))  # array filled with horizontal means

    # if you exceed the number of dimensions, you'll get a 'numpy.AxisError'
    try:
        print(ordered_data.mean(axis=3))
    except np.AxisError as axis_error:
        print(axis_error)
