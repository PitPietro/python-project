import numpy as np

from math_study.numpy_basics.data_types.data_types_list import data_type, table_of_data_types


def print_info(_array: np.array):
    print('{} \n\t 1. dtype = {}\n\t 2. item size = {}\n\t 3. n° of bytes = {}\n'
          .format(_array, _array.dtype, _array.itemsize, _array.nbytes))


def create_array_from_type(_type: data_type, n_elements: int):
    # print(_type.get('type'))
    return np.array(list(range(n_elements)), _type.get('type'))


if __name__ == '__main__':
    print('NumPy Data Types - Print data type info:\n')
    for _data_type in table_of_data_types:
        _array = create_array_from_type(_data_type, 10)
        print_info(_array)

