"""
> Task
You are given an array of integers representing coordinates of obstacles situated on a straight line.
Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to
make jumps of the same length represented by some integer. Find the minimal length of the jump
enough to avoid all the obstacles.

> Example
For inputArray = [5, 3, 6, 7, 9], the output should be 4.
Check out the image below for better understanding: (/code_signal_images/avoid_obstacles.png)

> Input/Output
- execution time limit: 4 seconds (py3))
- input: array.integer inputArray
Non-empty array of positive integers.
- guaranteed constraints:
2 ≤ inputArray.length ≤ 1000,
1 ≤ inputArray[i] ≤ 1000.
- output: integer
The desired length.
"""
from python_structure.code_signal_challenges.result_is_correct import is_correct


def avoid_obstacles(i_list):
    pass


if __name__ == '__main__':
    is_correct(avoid_obstacles([5, 3, 6, 7, 9]), 4)
    is_correct(avoid_obstacles([2, 3]), 4)
    is_correct(avoid_obstacles([1, 4, 10, 6, 2]), 7)
    is_correct(avoid_obstacles([1000, 999]), 6)
    is_correct(avoid_obstacles([19, 32, 11, 23]), 3)
    is_correct(avoid_obstacles([5, 8, 9, 13, 14]), 6)
