import numpy as np

from math_study.numpy_basics.statistics.statistics import random_data

if __name__ == '__main__':
    print('Numpy - Statistic - min & max')

    print('\nrandom multidimensional array:')
    print(random_data)

    print('get the min value from the array:')
    print(random_data.min())

    print('\nget the min value from the array along the specified axis:')
    print(random_data.min(axis=0))  # array filled with vertical min values: min of the values in the same column
    print(random_data.min(axis=1))  # array filled with horizontal min values: min of the values in the same rows

    # if you exceed the number of dimensions, you'll get a 'numpy.AxisError'
    try:
        print(random_data.min(axis=3))
    except np.AxisError as axis_error:
        print(axis_error)

    print(str('- ' * 20))

    print('get the max value from the array:')
    print(random_data.max())

    print('\nget the min value from the array along the specified axis:')
    print(random_data.max(axis=0))  # array filled with vertical max values: max of the values in the same column
    print(random_data.max(axis=1))  # array filled with horizontal max values: max of the values in the same rows

    # if you exceed the number of dimensions, you'll get a 'numpy.AxisError'
    try:
        print(random_data.max(axis=3))
    except np.AxisError as axis_error:
        print(axis_error)
