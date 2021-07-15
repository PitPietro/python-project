import numpy as np

if __name__ == '__main__':
    # .npy file extension have the fastest method of loading in data (even faster than .csv)
    # .npz file extension [...]

    print('Numpy - Write & Read - .npy')
    array = np.arange(20)

    print('\narray:')
    print(array)

    print('\nsaving array to .npy file')
    np.save('ARRAY', array)

    print('\nload array from .npy file')
    loaded_array = np.load('ARRAY.npy')
    print(loaded_array)

    print('Numpy - Write & Read - .npz')
    array1 = np.arange(15)
    array2 = np.arange(2, 5)

    print('\narrays:')
    print(array1)
    print(array2)

    print('\nsaving arrays to .npz file with keys')
    np.savez('ARRAYS', key1=array1, key2=array2)

    print('\nload arrays from .npz file')
    loaded_arrays = np.load('ARRAYS.npz')
    print(loaded_arrays['key1'])
    print(loaded_arrays['key2'])

    print('\nsaving arrays to .npz file with keys in a compressed way')
    np.savez_compressed('ARRAYS_COMPRESSED', key1=array1, key2=array2)

    print('\nload arrays from .npz file')
    loaded_arrays = np.load('ARRAYS_COMPRESSED.npz')
    print(loaded_arrays['key1'])
    print(loaded_arrays['key2'])
