import numpy as np

from math_study.numpy_basics.data_types.print_data_type_info import print_info

if __name__ == '__main__':
    int_array = np.array(list(range(10)), dtype=np.int64)
    float_array = np.array(list(range(10)), dtype=np.float128)
    complex_array = np.array(list(range(10)), dtype=np.complex256)

    int_to_float_array = int_array.astype(np.float128)
    int_to_complex_array = int_array.astype(np.complex256)
    float_to_int_array = int_array.astype(np.int64)
    float_to_complex_array = int_array.astype(np.complex256)
    complex_to_int_array = int_array.astype(np.int64)
    complex_to_float_array = int_array.astype(np.float128)

    _arrays = [
        int_to_float_array, int_to_complex_array,
        float_to_int_array, float_to_complex_array,
        complex_to_int_array, complex_to_float_array
    ]

    for _array in _arrays:
        print_info(_array)
