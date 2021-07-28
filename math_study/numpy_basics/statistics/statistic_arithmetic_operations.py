import numpy as np

# from math_study.numpy_basics.statistics.statistics import ordered_data

if __name__ == '__main__':
    print('Numpy - Statistic - Arithmetic Operations in ndarrays')

    # print('\nordered multidimensional array')
    # print(ordered_data)

    array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    array2 = np.array([[4, 5, 6], [7, 8, 9]])

    print('\nmoltiplication between numpy arrays')
    print(array1 * 2)
    print(array1 * array1)
    print('\nplease note: arrays must have the same shape')
    try:
        print(array1 * array2)
    except ValueError as e:
        print(e)  # ValueError: operands could not be broadcast together with different shapes

    print('\naddition between numpy arrays')
    print(array1 + 2)
    print(array1 + array1)
    print('\nplease note: arrays must have the same shape')
    try:
        print(array1 + array2)
    except ValueError as e:
        print(e)  # ValueError: operands could not be broadcast together with different shapes


    print('\nsubtraction between numpy arrays')
    print(array1 - 2)
    print(array1 - array1)
    print('\nplease note: arrays must have the same shape')
    try:
        print(array1 - array2)
    except ValueError as e:
        print(e)  # ValueError: operands could not be broadcast together with different shapes

    print('\nreciprocal of numpy array')
    reciprocal_array = np.array(1 / array1, dtype=np.float64)
    print(reciprocal_array)

    print('\npower of numpy array')
    print(array1 ** 2)
    print(array1 ** array1)
    print('\nplease note: arrays must have the same shape')
    try:
        print(array1 ** array2)
    except ValueError as e:
        print(e)  # ValueError: operands could not be broadcast together with different shapes