import numpy as np
import copy


if __name__ == '__main__':
    # np.copy is a shallow copy and will not copy object elements within arrays

    # numpy array of objects
    numpy_object_array = np.array([0, 'a', [1, 2, 3], 'word', [1.2, 2.3, 3.4]], dtype=object)
    print(numpy_object_array)

    copy_array = np.copy(numpy_object_array)

    # even using np.copy(), the copied array of objects is modified by the other array
    copy_array[2][2] = 9
    print(numpy_object_array)

    # to ensure all elements within an object array are copied, use copy.deepcopy()
    print('\n-----\n')
    numpy_object_array = np.array([0, 'a', [1, 2, 3], 'word', [1.2, 2.3, 3.4]], dtype=object)
    print(numpy_object_array)

    deep_copy_array = copy.deepcopy(numpy_object_array)

    deep_copy_array[2][2] = 9
    print(numpy_object_array)

# https://numpy.org/doc/stable/reference/generated/numpy.copy.html
