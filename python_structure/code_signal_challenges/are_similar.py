"""
> Task
Two arrays are called similar if one can be obtained from another by
swapping at most one pair of elements in one of the arrays.
Given two arrays a and b, check whether they are similar.

> Example
For a = [1, 2, 3] and b = [1, 2, 3], the output should be true.
The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be true.
We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be false.
Any swap of any two elements either in a or in b won't make a and b equal.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: array.integer a & array.integer b
a is an array of integers and b is an array of integers of the same length as a.
- guaranteed constraints:
3 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ 1000.
b.length = a.length,
1 ≤ b[i] ≤ 1000.
- output: boolean
true if a and b are similar, false otherwise.
"""


def are_similar():
    pass


if __name__ == '__main__':
    are_similar()
