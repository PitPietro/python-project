import numpy as np

from math_study.numpy_basics.statistics.statistics import statistic_function_over_axis, ordered_data

if __name__ == '__main__':
    print('Numpy - Statistic - sum')

    print('\nordered multidimensional array')
    print(ordered_data)

    print('\nget the sum of the whole array:')
    print(ordered_data.sum())

    print('\nget the sum of the array along the specified axis:')
    for i in range(3):
        statistic_function_over_axis(np.sum, ordered_data, i)

    ordered_data = np.array([[np.arange(10), np.arange(10, 20)], [np.arange(30, 40), np.arange(50, 60)]])
    print('\nnew ordered multidimensional array')
    print(ordered_data)

    print('\nget the sum of the new array along the specified axis:')
    for i in range(4):
        statistic_function_over_axis(np.sum, ordered_data, i)
