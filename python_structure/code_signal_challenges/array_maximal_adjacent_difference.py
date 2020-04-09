"""
> Task
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

> Example
For inputArray = [2, 4, 1, 0], the output should be 3.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: array.integer inputArray
- guaranteed constraints:
3 ≤ inputArray.length ≤ 10 & -15 ≤ inputArray[i] ≤ 15.
- output: integer
The maximal absolute difference.
"""


def array_maximal_adjacent_difference(input_array):
    abs_diff = 0
    for i in range(len(input_array) - 1):
        diff = abs(input_array[i] - input_array[i + 1])
        print("diff: {} =  {} - {}".format(diff, input_array[i], input_array[i + 1]))
        if diff > abs_diff:
            abs_diff = diff
    return abs_diff


def array_maximal_adjacent_difference_v2(input_array):
    abs_diff = []
    for i in range(len(input_array) - 1):
        abs_diff.append(abs(input_array[i] - input_array[i + 1]))
    return max(abs_diff)


if __name__ == '__main__':
    # 3
    print(array_maximal_adjacent_difference([2, 4, 1, 0]))
    print(array_maximal_adjacent_difference_v2([2, 4, 1, 0]))
    # 0
    print(array_maximal_adjacent_difference([1, 1, 1, 1]))
    # 7
    print(array_maximal_adjacent_difference([-1, 4, 10, 3, -2]))
    # 2
    print(array_maximal_adjacent_difference([10, 11, 13]))
    # 0
    print(array_maximal_adjacent_difference([-2, -2, -2, -2, -2]))
    # 4
    print(array_maximal_adjacent_difference([-1, 1, -3, -4]))
    # 30
    print(array_maximal_adjacent_difference([-14, 15, -15]))
