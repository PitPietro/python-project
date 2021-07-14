import numpy as np
import time

N = 10000000  # 10'000'000 data points


def save_to_npy(data_array):
    np.save('compare/data.npy', data_array)

    start = time.time()

    data_array = np.load('compare/data.npy')

    end = time.time()

    read_time = round(end - start, 5)
    print("\n___ .npy ___")
    print("\ndata summary:\n", data_array)
    print("\ndata shape:\n", data_array.shape)
    print(f"\nTime to read: {read_time} seconds.")
    return read_time


def save_to_csv(data_array):
    pass


def save_to_txt():
    start = time.time()

    with open('compare/data.txt', 'w') as txt_data:
        for _ in range(N):
            txt_data.write(str(10 * np.random.random()) + ',')

    with open('compare/data.txt', 'r') as txt_data:
        string_data = txt_data.read()

    list_data = string_data.split(',')
    list_data.pop()
    data_array = np.array(list_data, dtype=float).reshape(10000, 1000)

    end = time.time()

    read_time = round(end - start, 5)
    print("\n___ .txt ___")
    print("\ndata summary:\n", data_array)
    print("\ndata shape:\n", data_array.shape)
    print(f"\nTime to read: {read_time} seconds.")
    return read_time, data_array


if __name__ == '__main__':
    print('Numpy - .npy vs .csv vs .txt')
    print(f'\nWrite {N} points of data that will be read and saved in the different file formats.')

    txt_time, data = save_to_txt()

    save_to_csv(data)

    save_to_npy(data)

# https://towardsdatascience.com/what-is-npy-files-and-why-you-should-use-them-603373c78883
