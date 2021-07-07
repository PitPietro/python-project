import numpy as np

if __name__ == '__main__':
    print('Numpy - Boolean Indexing & Slicing')

    words = np.array(['Hi', 'Ho', 'Ha', 'He', 'Hu', 'Ha', 'Ha', 'Hu'])
    data = np.array([
        np.linspace(0, 10, 10, dtype=np.int16),
        np.linspace(10, 19, 10, dtype=np.int16),
        np.linspace(20, 29, 10, dtype=np.int16),
        np.linspace(30, 39, 10, dtype=np.int16),
        np.linspace(40, 49, 10, dtype=np.int16),
        np.linspace(50, 59, 10, dtype=np.int16),
        np.linspace(60, 69, 10, dtype=np.int16),
        np.linspace(70, 79, 10, dtype=np.int16),
    ])

    print('\nmeaningless list of words')
    print(words)

    print('\nordered list of integers')
    print(data)

    print("\ncheck where is the given element in the array and return an array filled with 'True' or 'False'")
    print(words == 'He')

    print("\ncheck where there is not the given element in the array and return an array filled with 'True' or 'False'")
    print(words != 'He')

    print('\n(negate the condition in a different way)')
    print(~(words == 'He'))

    # 'data' is a multidimensional array filled with ordered number (to make easier to understand)
    # returns the sub-arrays corresponding to the indexes equal to 'True' depending on the statement in the []
    print("\ntake the arrays corresponding to the indexes which the condition set to 'True'")
    print(data[words == 'Hu'])

    print('\n(negate the condition)')
    print(data[~(words == 'Hu')])

    print('\nsave the condition in a variable')
    condition = (words == 'Ha')
    print(condition)
    print('\ntake the arrays corresponding to the indexes by negating the saved condition')
    print(data[~condition])

    print('\nsave the multiple condition in a variable')
    multiple_condition = (words == 'Ha') | (words == 'He')
    print(multiple_condition)
    print("\ntake the arrays corresponding to the indexes which the multiple condition set to 'True'")
    print(data[multiple_condition])
    print("\n(negate the multiple condition)")
    print(data[~multiple_condition])

    print("\nmoreover, slice the output result (in different ways)")
    print(data[words == 'Hu', :])
    print('')
    print(data[words == 'Hu', 2:])
    print('')
    print(data[words == 'Hu', :4])
    print('')
    print(data[words == 'Hu', 1:4])

    print('\ncreate an array from the condition and the given index position')
    print(data[words == 'Hu', 3])

    print('\nfilter the data where the array elements correspond to the given condition and assign them')
    tmp_data = np.copy(data)  # use a copy of the array to avoid reassign the whole data (demonstration purpose only)
    tmp_data[tmp_data < 40] = 0
    print(tmp_data)
    print('\n(conditions can be different)')
    tmp_data = np.copy(data)  # copy again the data array to let the test starting from the "standard" data
    tmp_data[words == 'Hi'] = 0
    print(tmp_data)

# https://numpy.org/doc/stable/reference/generated/numpy.copy.html
