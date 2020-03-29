"""
> Task
Two people live in the same house. Each of the rooms has a different cost, and some of them are
free, but there's a rumour that all the free rooms are haunted! Since they are quite superstitious,
they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your
task is to return the total sum of all rooms that are suitable for them (ie: add up all the values
hat don't appear below a 0).

> Example
Given this matrix input:
matrix = [[0, 1, 1, 2],
        [0, 5, 0, 0],
        [2, 0, 3, 3]]

The output should be 9 (see 'matrix_example1.png').
There are several haunted rooms, so we'll disregard them as well as any rooms beneath them.
Thus, the answer is 1 + 5 + 1 + 2 = 9.

Given this matrix input:
matrix = [[1, 1, 1, 0],
        [0, 5, 0, 1],
        [2, 1, 3, 10]]

The output should be 9 (see 'matrix_example2.png')..
Note that the free room in the final column makes the full column unsuitable for the couple
(not just the room directly beneath it).
Thus, the answer is 1 + 1 + 1 + 5 + 1 = 9.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: array.array.integer matrix
A 2-dimensional array of integers representing the cost of each room in the building.
A value of 0 indicates that the room is haunted.
- guaranteed constraints:
1 ≤ matrix.length ≤ 5,
1 ≤ matrix[i].length ≤ 5,
0 ≤ matrix[i][j] ≤ 10.
- output: integer
The total price of all the rooms that are suitable for the people to live in.
"""


def matrix_elements_sum(matrix):
    sum = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            sum += matrix[row][col]
            print("sum: {}\t row: {}\tcol: {}\t matrix[row][col]: {}".format(sum, row, col, matrix[row][col]))
    return sum


def matrix_task_elements_sum(matrix):
    sum = 0
    # col number where there's a zero
    zeros = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                zeros.append(col)
            can_add = True
            for el in zeros:
                if col == el:
                    can_add = False

            if can_add:
                sum += matrix[row][col]
            print("sum: {}\t row: {}\tcol: {}\t matrix[row][col]: {}\t can add: {}"
                  .format(sum, row, col, matrix[row][col], can_add))
    return sum


if __name__ == '__main__':
    matrix_zero = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    matrix1 = [[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]
    matrix2 = [[1, 1, 1, 0], [0, 5, 0, 1], [2, 1, 3, 10]]
    matrix3 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    matrix4 = [[0]]
    matrix5 = [[1, 0, 3], [0, 2, 1], [1, 2, 0]]
    matrix6 = [[1], [5], [0], [2]]
    matrix7 = [[1, 2, 3, 4, 5]]
    matrix8 = [[2], [5], [10]]
    matrix9 = [[4, 0, 1], [10, 7, 0], [0, 0, 0], [9, 1, 2]]
    matrix10 = [[1]]

    print("Just try a matrix sum", matrix_elements_sum(matrix_zero))

    print(matrix_task_elements_sum(matrix1))
    print(matrix_task_elements_sum(matrix2))
    print(matrix_task_elements_sum(matrix3))
    print(matrix_task_elements_sum(matrix4))
    print(matrix_task_elements_sum(matrix5))
    print(matrix_task_elements_sum(matrix6))
    print(matrix_task_elements_sum(matrix7))
    print(matrix_task_elements_sum(matrix8))
    print(matrix_task_elements_sum(matrix9))
    print(matrix_task_elements_sum(matrix10))
