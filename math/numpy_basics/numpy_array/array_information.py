import numpy as np
from array_creation import py_arrays


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


if __name__ == '__main__':
    print('Numpy Array - Info\n')
    print('number of axes: ' + str(number_of_axes(py_arrays)))
    print('shape: ' + str(shape(py_arrays)))
    print('n° of elements: ' + str(size(py_arrays)))
    print('dtype: ' + str(dtype(py_arrays)))
    print('item size: ' + str(item_size(py_arrays)))
    print('data: ' + str(data(py_arrays)))


# switch-case: https://www.simplifiedpython.net/python-switch-case-statement/
