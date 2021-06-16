# All the elements in a NumPy array should be homogeneous. Mathematical operations that are meant to be
# performed on arrays would be extremely inefficient if the arrays were not homogeneous.
# NumPy arrays are faster than Python lists: an array consumes less memory and is convenient to use.
# NumPy uses much less memory to store data and provides a mechanism of specifying the data types.
#
# Elements inside an array are all of the same type, referred to as the array 'dtype'.
#
# 'ndarray' is a shorthand for 'N-dimensional array'.
# An N-dimensional array is an array with any number of dimensions.
# NumPy 'ndarray' class is used to represent both matrices and vectors.
# A vector is an array with a single dimension (no difference between row and column vectors).
# A matrix refers to an array with two dimensions.
# For 3-D or higher dimensional arrays, 'tensor' is also commonly used as term.
#
# An array can be indexed by a tuple of non-negative integers, by booleans, by another array, or by integers.
# The rank of the array is the number of dimensions.
# The shape of the array is a tuple of integers giving the size of the array along each dimension.
#
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


def init_np_array(array, numpy_type=int) -> object:
    """
    Parameters
    ----------
    array Python array

    Returns
    -------
    Create a NumPy array from a Python array
    """
    return np.array(array, dtype=numpy_type)


def number_of_axes(array):
    """
    Parameters
    ----------
    array Python array

    Returns
    -------
    Number of axes (dimensions) of the array.
    """
    return np.array(array).ndim


def shape(array):
    """
    The dimension of the array is a tuple of integers indicating the size of the array in each dimension.
    For a matrix with n rows and m columns, shape will be (n,m).
    The length of the shape tuple is therefore the number of axes, ndim.
    Parameters
    ----------
    array Python array

    Returns
    -------
    Dimensions of the array.
    """
    return np.array(array).shape


def size(array):
    """
    Parameters
    ----------
    array Python array Python array

    Returns
    -------
    Total number of elements of the array. It is equal to the product of the elements of shape.
    """
    return np.array(array).size


def dtype(array):
    """
    One can create or specify dtype's using standard Python types.
    NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.
    Parameters
    ----------
    array Python array

    Returns
    -------
    Object describing the type of the elements in the array.
    """
    return np.array(array).dtype


def item_size(array):
    """

    Parameters
    ----------
    array Python array

    Returns
    -------
    Size in bytes of each element of the array.
    """
    return np.array(array).itemsize


def data(array):
    """
    Parameters
    ----------
    array Python array

    Returns
    -------
    The buffer containing the actual elements of the array.
    You do not usually need to use this attribute: you will access the elements in an array using indexing facilities.
    """
    return np.array(array).data


def zeros(n, m, numpy_type=np.float64):
    """
    Elements of an array are originally unknown, but its size could be known.
    NumPy offers several functions to create arrays with initial placeholder
    content, which minimize the necessity of growing arrays (an expensive operation).

    By default, the dtype of the created array is float64.

    Parameters
    ----------
    n number of dimensions
    m number of elements for each dimension
    numpy_type dtype

    Returns
    -------
    Array full of zeros
    """
    return np.zeros((n, m), dtype=numpy_type)


def ones(n, m, numpy_type=np.float64):
    """
    Parameters
    ----------
    n number of dimensions
    m number of elements for each dimension
    numpy_type dtype

    Returns
    -------
    Array full of ones
    """
    return np.ones((n, m), dtype=numpy_type)


def empty(n, m, numpy_type=np.float64):
    """
    Parameters
    ----------
    n number of dimensions
    m number of elements for each dimension
    numpy_type dtype

    Returns
    -------
    Array full of random values which depends on the state of the memory
    """
    return np.empty((n, m), dtype=numpy_type)


def range_of_elements(start, end, step, numpy_type=None):
    """
    NumPy provides the 'arange' function which is analogous to the Python built-in 'range', but returns an array.
    Parameters
    ----------
    start start of the array
    end end of the array
    step value to increment for each element in the array
    numpy_type type of the elements inside the array

    Returns
    -------
    Sequences of numbers from 'start' to 'end', which are a summation of 'step'
    """
    return np.arange(start, end, step, dtype=numpy_type)


if __name__ == '__main__':
    complex_py_array = [-1, -2, -3, -4, -5]
    py_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    py_arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    print('mono-dimensional array:\n' + str(init_np_array(py_array)))
    print('\nmono-dimensional array (complex):\n{}'.format(str(init_np_array(complex_py_array, complex))))
    print('\nn-dimensional array:\n' + str(init_np_array(py_arrays)))
    print('number of axes: ' + str(number_of_axes(py_arrays)))
    print('shape: ' + str(shape(py_arrays)))
    print('n° of elements: ' + str(size(py_arrays)))
    print('dtype: ' + str(dtype(py_arrays)))
    print('item size: ' + str(item_size(py_arrays)))
    print('data: ' + str(data(py_arrays)))
    print('-------')
    print('zeros:\n' + str(zeros(2, 5, np.int16)))
    print('zeros:\n' + str(zeros(3, 4)))
    print('-------')
    print('ones:\n' + str(ones(2, 3, np.int16)))
    print('ones:\n' + str(ones(4, 2)))
    print('-------')
    print('empty:\n' + str(empty(1, 4, np.int16)))
    print('empty:\n' + str(empty(4, 3)))
    print('-------')
    print('arange:\n' + str(range_of_elements(1, 4, 0.5)))

# https://numpy.org/doc/stable/user/quickstart.html
