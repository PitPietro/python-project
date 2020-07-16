"""
> Task
Given an n-interesting polygon. The task is to find the area of a polygon for a given n.
A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon
is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons
to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in 'shape_area.png'.

> Example
For n = 2, the output should be shapeArea(n) = 5;
For n = 3, the output should be shapeArea(n) = 13.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: integer n
- guaranteed constraints:
1 ≤ n < 104.
- output: integer
The area of the n-interesting polygon.
"""
import sys
sys.setrecursionlimit(1000000)


def shape_area(n):
    if n < 1:
        pass
    elif n == 1:
        return n
    else:
        tmp_n = n - 1
        return tmp_n * 4 + shape_area(tmp_n)


def shape_area_v2(n):
    return n**2 + (n-1)**2


if __name__ == '__main__':
    for i in range(-5, 104):
        msg = "n°{} --> {}\t{}"
        print(msg.format(i, shape_area(i), shape_area_v2(i)))

