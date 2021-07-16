import numpy as np

if __name__ == '__main__':
    print('Numpy - Statistic')

    random_data = np.random.randn(2, 4)
    ordered_data = np.array([np.arange(10), np.arange(10, 20)])

    print('\nrandom multidimensional array:')
    print(random_data)
    print('\nordered multidimensional array')
    print(ordered_data)

    # https://numpy.org/doc/stable/reference/generated/numpy.mean.html
    print('\nCompute the arithmetic mean of the whole array:')
    print(ordered_data.mean())

    print('\nCompute the arithmetic mean along the specified axis:')
    print(ordered_data.mean(axis=0))  # array filled with vertical means
    print(ordered_data.mean(axis=1))  # array filled with horizontal means

    # if you exceed the number of dimensions, you'll get a 'numpy.AxisError'
    try:
        print(ordered_data.mean(axis=3))
    except np.AxisError as axis_error:
        print(axis_error)
