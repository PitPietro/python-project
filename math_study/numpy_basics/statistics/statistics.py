import numpy
import numpy as np

random_data = np.random.randn(2, 4)
ordered_data = np.array([np.arange(10), np.arange(10, 20)])


def statistic_function_over_axis(numpy_function: np.core.fromnumeric, data, axis: int):
    # a: array_like. Elements to apply the given 'np.core.fromnumeric' function.
    try:
        print(numpy_function(a=data, axis=axis))
    except np.AxisError as axis_error:
        print(axis_error)


if __name__ == '__main__':
    print('Numpy - Statistic')

    # utility arrays
    print('\nrandom multidimensional array:')
    print(random_data)
    print('\nordered multidimensional array')
    print(ordered_data)

# other useful function
# https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html
# https://numpy.org/doc/stable/reference/generated/numpy.std.html
