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
Note that the free room in the final column makes the full column unsuitable for bots
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
    pass


if __name__ == '__main__':
    matrix_elements_sum(123)
