import numpy as np
import time

from math_study.numpy_basics.data_types.print_data_type_info import print_info

ELEMENTS = 10000000  # 10'000'000 data points


def write_to_npy(data_array: np.array) -> float:
    start = time.time()
    np.save('compare/data.npy', data_array)
    end = time.time()

    read_time = round(end - start, 5)
    print("\n____________ write to .npy ________________________________________________")
    print_info(data_array)
    print(f"Time to write: {read_time} seconds.")
    print("___________________________________________________________________________")
    return read_time


def write_to_csv(data_array: np.array) -> float:
    start = time.time()
    np.savetxt('compare/data.csv', data_array, delimiter=',')
    end = time.time()

    read_time = round(end - start, 5)
    print("\n____________ write to .csv ________________________________________________")
    print_info(data_array)
    print(f"Time to write: {read_time} seconds.")
    print("___________________________________________________________________________")
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
    print("\n____________ write to .txt ________________________________________________")
    print_info(data_array)
    print(f"Time to write: {read_time} seconds.")
    print("___________________________________________________________________________")
    return read_time


if __name__ == '__main__':
    print('Numpy - .npy vs .csv vs .txt')
    print(f'\nWrite {ELEMENTS} points of data that will be read and saved in the different file formats.')

    data = np.random.rand(ELEMENTS)
    print(data)

    write_time_npy = write_to_npy(data)
    write_time_csv = write_to_csv(data)
    write_time_txt = write_to_txt(data)

# https://towardsdatascience.com/what-is-npy-files-and-why-you-should-use-them-603373c78883
