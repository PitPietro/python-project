import numpy as np

random_data = np.random.randn(2, 4)
ordered_data = np.array([np.arange(10), np.arange(10, 20)])

if __name__ == '__main__':
    print('Numpy - Statistic')

    # utility arrays
    print('\nrandom multidimensional array:')
    print(random_data)
    print('\nordered multidimensional array')
    print(ordered_data)
