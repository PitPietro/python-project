import numpy as np


if __name__ == '__main__':
    print('Numpy - Fancy Indexing')

    data = np.zeros((8, 4))

    print('\nempty multidimensional array')
    print(data)

    for i in range(8):
        data[i] = i ** 2

    print('\nfor-loop modified the multidimensional array')
    print(data)

    print('\nget the sub-arrays whose indexes are specified by the integer list')
    integer_list = [5, 2, 3, 7]
    print(data[integer_list])

    # negative indexes slice the array from the end: array[-1] is the last element of array
    print('\nget the sub-arrays whose indexes are specified by the list of negative integers')
    negative_integer_list = [-5, -2, -3, -7]
    print(data[negative_integer_list])

    print('\nreshape the array')
    try:
        data_reshape = data.reshape((2, 17))
        print(data_reshape)
    except ValueError as error:
        print(error)

    try:
        data_reshape = data.reshape((2, 16))
        print(data_reshape)
    except ValueError as error:
        print(error)

    print('\nslice the array given a couple of list')
    data = np.arange(32).reshape((8, 4))
    list1, list2 = [2, 4], [3, 1]
    # the first list gives the index of the sub-arrays
    # the second list gives the index of the elements
    print(data[list1, list2])
