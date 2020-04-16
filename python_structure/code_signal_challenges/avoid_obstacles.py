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
    i_list.sort()
    result = 1
    my_range = i_list[-1] + 2
    for i in range(1, my_range):
        print("i: {}".format(i))
        if i in i_list:
            print("i is in the list")
        tmp_r = result
        tmp_list = list()
        tmp_list.append(tmp_r)
        for j in range(my_range):
            tmp_r += i
            tmp_list.append(tmp_r)
            print("j: {}|\tr: {}\tlist: {}".format(j, tmp_r, tmp_list))
        result += 1
    print(i_list)


if __name__ == '__main__':
    is_correct(avoid_obstacles([5, 3, 6, 7, 9]), 4)
    # is_correct(avoid_obstacles([2, 3]), 4)
    # is_correct(avoid_obstacles([1, 4, 10, 6, 2]), 7)
    # is_correct(avoid_obstacles([1000, 999]), 6)
    # is_correct(avoid_obstacles([19, 32, 11, 23]), 3)
    # is_correct(avoid_obstacles([5, 8, 9, 13, 14]), 6)
