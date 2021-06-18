# Arithmetic operators on arrays apply elementwise.
# A new array is created and filled with the result.
import numpy as np
from array_creation import range_of_elements_given_number, ones


def arithmetic_operations(array1, array2, operation: ''):
    """
    Arithmetic operations are possible:
    1. only between arrays with the same number of element foreach dimension
    2. with arrays of different dimension.
    Parameters
    ----------
    array1
    array2
    operation

    Returns
    -------

    """
    try:
        if operation == '+':
            return array1 + array2
        if operation == '-':
            return array1 - array2
        if operation == '*':
            return array1 * array2
        if operation == '/':
            return array1 / array2
    except ValueError as e:
        return 'Error: ' + str(e)


if __name__ == '__main__':
    print('Numpy Array - Operations\n')
    a = np.linspace(1, 8, 8)
    b = ones(2, 8)
    # print(a)
    # print(b)
    print('arithmetic sum:\n' + str(arithmetic_operations(a, b, '+')))
    print('arithmetic diff:\n' + str(arithmetic_operations(a, b, '-')))
    print('arithmetic *\n' + str(arithmetic_operations(a, b, '*')))
    print('arithmetic /\n' + str(arithmetic_operations(a, b, '/')))
