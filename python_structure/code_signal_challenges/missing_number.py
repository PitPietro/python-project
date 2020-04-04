"""
https://app.codesignal.com/challenge/p4qArskGsNtf6ecdP

> Task
You are supposed to label a bunch of boxes with numbers from 0 to n, and all the labels are stored in the array arr.
Unfortunately one of the labels is missing. Your task is to find it.

> Example
For arr = [3, 1, 0], the output should be 2.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: array.integer arr
An unsorted array consisting of different integers from 0 to n inclusive, with only one of them missing.
- guaranteed constraints:
1 ≤ arr.length ≤ 1000,
0 ≤ arr[i] ≤ arr.length.
- output: integer
The missing number.
"""


def missing_number(array):
    array.sort()
    num = 0
    if array == [0]:
        return 1
    elif array[0] > 0:
        return 0
    for i, j in enumerate(array):
        print("i: {}| j: {}| array: {}| num: {}".format(i, j, array, num))
        if num == j:
            num += 1
        elif num != j:
            return num
        print("i: {}| j: {}| array: {}| num: {}".format(i, j, array, num))
    return num


if __name__ == '__main__':
    # 2
    test_1 = [3, 1, 0]
    # 1
    test_2 = [0]
    # 0
    test_3 = [1, 2]
    # 2
    test_4 = [0, 1]
    # 0
    test_5 = [3, 1, 2]
    # 0
    test_6 = [3, 2, 1]
    # 4
    test_7 = [5, 2, 1, 6, 3, 0]
    # 1
    test_8 = [8, 6, 7, 0, 2, 5, 4, 3]
    # 9
    test_9 = [0, 3, 5, 8, 4, 6, 1, 9, 7]
    # 0
    test_10 = [2, 9, 8, 1, 3, 6, 7, 4, 5]
    # 8
    test_11 = [9, 6, 4, 2, 3, 5, 7, 0, 1]

    print(missing_number_v2(test_9))
