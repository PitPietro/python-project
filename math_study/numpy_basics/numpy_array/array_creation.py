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

complex_py_array = [-1, -2, -3, -4, -5]
py_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
py_arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]


def init_np_array(array, numpy_type=int) -> object:
    """
    Parameters
    ----------
    array Python array

    Returns
    -------
    object
    Create a NumPy array from a Python array
    """
    return np.array(array, dtype=numpy_type)


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
    n : int
      Number of dimensions
    m: int
      Number of elements for each dimension
    numpy_type : data-type, optional
      Data-type of the returned array.

    Returns
    -------
    Array full of random values which depends on the state of the memory.
    """
    return np.empty((n, m), dtype=numpy_type)


def eye(n, m=None, k=0, numpy_type=np.float, numpy_order='C'):
    """
    Parameters
    ----------
    n : int
      Number of rows in the output.
    m : int, optional
      Number of columns in the output. If None, defaults to `n`.
    k : int, optional
      Index of the diagonal: 0 (the default) refers to the main diagonal,
      a positive value refers to an upper diagonal, and a negative value
      to a lower diagonal.
    numpy_type : data-type, optional
      Data-type of the returned array.
    numpy_order : {'C', 'F'}, optional
        Whether the output should be stored in row-major (C-style) or
        column-major (Fortran-style) order in memory.

    Returns
    -------
    2-D array with ones on the diagonal and zeros elsewhere.
    """
    return np.eye(n, m, k, dtype=numpy_type, order=numpy_order)


def range_of_elements_given_step(start, end, step, numpy_type=None):
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


def range_of_elements_given_number(start, end, number, numpy_type=None):
    """
    Since is usually not possible to predict the number of elements obtained with
    'arange' function, due to the finite floating point precision, it is usually
    better to use 'linspace' function that receives as an argument the number of elements that we want, instead of the step:
    Parameters
    ----------
    start start of the array
    end end of the array
    number number of elements to insert in the NumPy array
    numpy_type type of the elements inside the array

    Returns
    -------
    Sequences of 'number' numbers from 'start' to 'end'
    """
    return np.linspace(start, end, number, dtype=numpy_type)


if __name__ == '__main__':
    print('Numpy Array - Creation\n')
    print('mono-dimensional array:\n' + str(init_np_array(py_array)))
    print('\nmono-dimensional array (complex):\n{}'.format(str(init_np_array(complex_py_array, complex))))
    print('\nn-dimensional array:\n' + str(init_np_array(py_arrays)))
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
    print('eye:\n' + str(eye(5)))
    print('eye:\n' + str(eye(3, 7)))
    print('-------')
    print('arange:\n' + str(range_of_elements_given_step(1, 4, 0.5)))
    print('linspace:\n' + str(range_of_elements_given_number(1, 8, 5)))

# https://numpy.org/doc/stable/user/quickstart.html
