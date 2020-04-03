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
    for i, j in enumerate(array):
        print("i: {}| j: {}| array: {}| num: {}".format(i, j, array, num))
        if num == j:
            num += 1
        else:
            array.append(num)
        print("i: {}| j: {}| array: {}| num: {}".format(i, j, array, num))
    temp = set(array)
    array = list(temp)
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

    print(missing_number(test_3))
