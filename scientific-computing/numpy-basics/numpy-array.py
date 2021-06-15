# All the elements in a NumPy array should be homogeneous. Mathematical operations that are meant to be
# performed on arrays would be extremely inefficient if the arrays were not homogeneous.
# NumPy arrays are faster than Python lists: an array consumes less memory and is convenient to use.
# NumPy uses much less memory to store data and provides a mechanism of specifying the data types.
#
# Elements inside an array are all of the same type, referred to as the array 'dtype'.
#
# An array can be indexed by a tuple of nonnegative integers, by booleans, by another array, or by integers.
# The rank of the array is the number of dimensions.
# The shape of the array is a tuple of integers giving the size of the array along each dimension.
#
# One way we can initialize NumPy arrays is from Python lists, using nested lists for two- or higher-dimensional data.
#
# An array can be indexed by:
# - a tuple of non-negative integers
# - booleans
# - another array
# - integers
#
# The rank of the array is the number of dimensions.
# The shape of the array is a tuple of integers giving the size of the array along each dimension.
#
# You can initialize NumPy arrays is from Python lists, using nested lists for n-dimensional data (with n > 1).

import numpy as np


def init_np_array():
    py_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    np_array = np.array(py_array)
    print(np_array)


def init_n_dim_np_array():
    py_arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    np_array = np.array(py_arrays)
    print(np_array)


if __name__ == '__main__':
    init_np_array()
    init_n_dim_np_array()
