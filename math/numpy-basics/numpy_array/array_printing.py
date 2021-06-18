# When printing an array, NumPy displays it in a similar way to nested lists, but with the following layout:
# - the last axis is printed from left to right,
# - the second-to-last is printed from top to bottom,
# - the rest are also printed from top to bottom, with each slice separated from the next by an empty line.
#
# One-dimensional arrays are printed as rows.
# Bi-dimensional arrays are printed as matrices.
# Tri-dimensional arrays are printed as lists of matrices.

import numpy as np
from array_creation import py_arrays


def print_one_dim_array(num):
    """
    'arange' function is used with only one parameter.
    If an array is too large to be printed, NumPy automatically skips the
    central part of the array and only prints the corners.
    To disable this behaviour and force NumPy to print the entire array, you can change the printing options.
    # >>> np.set_printoptions(threshold=sys.maxsize) # sys module should be imported
    Parameters
    ----------
    num number of elements to fill the NumPy array with

    Returns
    -------
    NumPy array filled with numbers from zero to 'dim'
    """
    return np.arange(num)


def reshape_n_dim_array(num, *dimensions):
    """
    The * is called unpacking operator. It allows the function to accept an indefinite number of arguments.
    This function tries to reshape the NumPy array based on the 'dimensions' parameters.
    If 'num' cannot be decomposed as a multiple of 'dimensions', it will throw a ValueError.
    Parameters
    ----------
    num number of elements to fill the NumPy array with
    dimensions the n dimensions whit which the array will be reshaped

    Returns
    -------
    An n-dimensional array
    """
    try:
        np_array = np.arange(num).reshape(*dimensions)
        return np_array
    except ValueError as e:
        return 'Error: ' + str(e)


if __name__ == '__main__':
    print('Numpy Array - Print\n')
    print('mono-dimensional array: ' + str(print_one_dim_array(10)))
    print('n-dimensional array:\n' + str(reshape_n_dim_array(8, 2, 4)))
    print('n-dimensional array:\n' + str(reshape_n_dim_array(24, 3, 7)))
    print('n-dimensional array:\n' + str(reshape_n_dim_array(8, 2, 2, 2)))
    print('---')
    print('very large mono-dimensional array:\n' + str(print_one_dim_array(5000)))
    print('very large n-dimensional array:\n' + str(reshape_n_dim_array(10000, 100, 100)))
