import time

import numpy as np

from math_study.numpy_basics.data_types.print_data_type_info import print_info

ELEMENTS = 10000000  # 10'000'000 data points


def write_to_npy(data_array: np.array) -> float:
    start = time.time()
    np.save('compare/data.npy', data_array)
    end = time.time()

    read_time = round(end - start, 5)
    print("\n____________ write to .npy _________________________________________________")
    print_info(data_array)
    print(f"Time to write: {read_time} seconds.")
    print("____________________________________________________________________________")
    return read_time


def write_to_csv(data_array: np.array) -> float:
    start = time.time()
    np.savetxt('compare/data.csv', data_array, delimiter=',')
    end = time.time()

    read_time = round(end - start, 5)
    print("\n____________ write to .csv _________________________________________________")
    print_info(data_array)
    print(f"Time to write: {read_time} seconds.")
    print("____________________________________________________________________________")
    return read_time


def write_to_txt(data_array: np.array) -> float:
    start = time.time()
    # np.savetxt('compare/data.txt', data_array, delimiter=' ')
    file = open('compare/data.txt', 'w+')
    for element in data_array:
        file.write(str(element) + '\n')
    file.close()
    end = time.time()

    read_time = round(end - start, 5)
    print("\n____________ write to .txt _________________________________________________")
    print_info(data_array)
    print(f"Time to write: {read_time} seconds.")
    print("____________________________________________________________________________")
    return read_time


def read_from_npy() -> float:
    start = time.time()
    data_array = np.load('compare/data.npy')
    end = time.time()

    read_time = round(end - start, 5)
    print("\n____________ read from .npy ________________________________________________")
    print_info(data_array)
    print(f"Time to read: {read_time} seconds.")
    print("____________________________________________________________________________")
    return read_time


def read_from_csv() -> float:
    start = time.time()
    data_array = np.loadtxt('compare/data.csv', delimiter=',')
    end = time.time()

    read_time = round(end - start, 5)
    print("\n____________ read from .csv ________________________________________________")
    print_info(data_array)
    print(f"Time to read: {read_time} seconds.")
    print("____________________________________________________________________________")
    return read_time


def read_from_txt() -> float:
    start = time.time()
    with open('compare/data.txt') as txt_file:
        data_array_list = txt_file.readlines()
    data_array = np.array(data_array_list)
    end = time.time()

    read_time = round(end - start, 5)
    print("\n____________ read from .txt ________________________________________________")
    print_info(data_array)
    print(f"Time to read: {read_time} seconds.")
    print("____________________________________________________________________________")
    return read_time


if __name__ == '__main__':
    print('Numpy - .npy vs .csv vs .txt')
    print(f'\nWrite {ELEMENTS} points of data that will be read and saved in the different file formats.')

    data = np.random.rand(ELEMENTS)
    print(data)

    # write_time_npy = write_to_npy(data)
    # write_time_csv = write_to_csv(data)
    # write_time_txt = write_to_txt(data)
    #
    # read_time_npy = read_from_npy()
    # read_time_csv = read_from_csv()
    read_time_txt = read_from_txt()

# https://datascienceparichay.com/article/read-csv-file-as-numpy-array/
