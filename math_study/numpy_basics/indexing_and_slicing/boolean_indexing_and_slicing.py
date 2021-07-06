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

    print("\ncheck where is an element in an array and return another array filled with 'True' or 'False'")
    print(words == 'He')

    # 'data' is a multidimensional array filled with ordered number (to make easier to understand)
    # returns the sub-arrays corresponding to the indexes equal to 'True' depending on the statement in the []
    print("\ntake the arrays corresponding to the indexes which the condition set to 'True'")
    print(data[words == 'Hu'])

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
