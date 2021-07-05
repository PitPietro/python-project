import numpy as np

if __name__ == '__main__':
    print('Numpy - Indexing & Slicing')

    int_array = np.array(np.arange(20))
    print('\nint array: ')
    print(int_array)

    print('\nget the element at the given index')
    print(int_array[3])

    print('\nslicing from 0 to the given end value')
    print(int_array[:4])

    print('\nslicing from start to end')
    print(int_array[5:10])

    print('\nassign a slice of the array, from start to end, to the given value')
    int_array[5:10] = 4
    print(int_array)

    print('\nassign the whole array elements to the given value')
    int_array[:] = 8
    print(int_array)

    print('\noverride the array with the given value')
    int_array = 8
    print(int_array)

    bi_dim_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print('\nbidimensional array')
    print(bi_dim_array)

    print('\nget the sub-array value at the given index')
    print(bi_dim_array[2])

    print('\nget the element at the given indexes')
    print(bi_dim_array[0][2])
    print(bi_dim_array[0, 2])

    print('\nslicing from 0 to the given end value')
    print(bi_dim_array[:2])

    print('\nslicing from 0 to the given end value, then take only the elements placed in the given position (2nd argument in the square brackets)')
    print(bi_dim_array[:2, 1])

    print('\n')
    print(bi_dim_array[:, 2])

    print('\nget the array filled by the elements placed in the given position (2nd argument in the square brackets)')
    print(bi_dim_array[:, 2])
