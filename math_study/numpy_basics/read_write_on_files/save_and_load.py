import numpy as np


if __name__ == '__main__':
    print('Numpy - Save & Load')
    # .npy file extension have the fastest method of loading in data (even faster than .csv)

    data = np.arange(20)

    print('\nbase data')
    print(data)

    print('\nsaving data to .npy file')
    np.save('DATA', data)

    print('\nload data from .npy file')
    loaded_data = np.load('DATA.npy')
    print(loaded_data)
