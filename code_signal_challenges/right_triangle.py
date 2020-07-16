"""
https://app.codesignal.com/tournaments/p9DLosRdmnyMewuri/D
> Task
For a given triangle determine if it is a right triangle.

> Example
For sides = [3, 5, 4], the output should be true.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: array.integer sides
Array of three integers representing triangle sides.
- guaranteed constraints:
2 ≤ sides[i] ≤ 20.
- output: boolean
true if the triangle with sides from the sides array is a right triangle, false otherwise.
"""
from code_signal_challenges.result_is_correct import is_correct


def right_triangle(sides):
    sides.sort()
    return sides[0]**2 + sides[1]**2 == sides[2]**2


if __name__ == '__main__':
    is_correct(right_triangle([3, 5, 4]), True)
    is_correct(right_triangle([2, 2, 2]), False)
    is_correct(right_triangle([9, 15, 6]), False)
    is_correct(right_triangle([3, 4, 4]), False)
    is_correct(right_triangle([4, 3, 5]), True)
    is_correct(right_triangle([3, 7, 5]), False)
    is_correct(right_triangle([13, 12, 5]), True)
    is_correct(right_triangle([4, 14, 11]), False)
    is_correct(right_triangle([8, 17, 15]), True)
    is_correct(right_triangle([9, 15, 20]), False)
