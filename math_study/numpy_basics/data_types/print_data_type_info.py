import numpy as np
from data_types_list import data_type, table_of_data_types


def print_info(_array: np.array):
    print('{} \n\t 1. dtype = {}\n\t 2. item size = {}\n\t 3. n° of bytes = {}\n'
          .format(_array, _array.dtype, _array.itemsize, _array.nbytes))


if __name__ == '__main__':
    print('NumPy Data Types - Print data type info:\n')
    print_info(np.array(list(range(10)), dtype=np.int16))
    print_info(np.array(list(range(10)), dtype=np.float32))
