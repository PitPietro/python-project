# All the elements in a NumPy array should be homogeneous. Mathematical operations that are meant to be
# performed on arrays would be extremely inefficient if the arrays were not homogeneous.
# NumPy arrays are faster than Python lists: an array consumes less memory and is convenient to use.
# NumPy uses much less memory to store data and provides a mechanism of specifying the data types.
#
# Elements inside an array are all of the same type, referred to as the array 'dtype'.
#
# An array can be indexed by a tuple of non-negative integers, by booleans, by another array, or by integers.
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


def init_np_array(array):
    """
    Initialize a NumPy array from a Python array
    """
    print(np.array(array))


def number_of_axes(array):
    """
    Number of axes (dimensions) of the array.
    """
    return np.array(array).ndim


def shape(array):
    """
    Dimensions of the array. It is a tuple of integers indicating the size of the array in each dimension.
    For a matrix with n rows and m columns, shape will be (n,m).
    The length of the shape tuple is therefore the number of axes, ndim.
    """
    return np.array(array).shape


def size(array):
    """
    Total number of elements of the array. It is equal to the product of the elements of shape.
    """
    return np.array(array).size


if __name__ == '__main__':
    py_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    py_arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    init_np_array(py_array)
    print('')
    init_np_array(py_arrays)
    print('number of axes: ' + str(number_of_axes(py_arrays)))
    print('shape: ' + str(shape(py_arrays)))
    print('n° of elements: ' + str(size(py_arrays)))
