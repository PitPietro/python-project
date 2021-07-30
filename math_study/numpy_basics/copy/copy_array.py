import numpy as np


if __name__ == '__main__':
    # basic numpy array
    numpy_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # copy the reference of the array: if you change one, the other will also be changed
    copy_by_reference_array = numpy_array

    # copy the value of the array: if you change one, the other will not be changed
    copy_by_value_array = np.copy(numpy_array)

    # make a change
    numpy_array[0] = 100

    print(copy_by_reference_array[0] == numpy_array[0])  # True
    print(copy_by_value_array[0] == numpy_array[0])  # False

# https://numpy.org/doc/stable/reference/generated/numpy.copy.html
