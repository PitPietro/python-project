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
    pass


if __name__ == '__main__':
    # 3
    print(array_maximal_adjacent_difference([2, 4, 1, 0]))
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
