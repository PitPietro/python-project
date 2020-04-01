"""
> Task
Some people are standing in a row in a park. There are trees between them which cannot be moved.
Your task is to rearrange the people by their heights in a non-descending order without moving
the trees. People can be very tall!

> Example
For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be [-1, 150, 160, 170, -1, -1, 180, 190].

> Input/Output
- execution time limit: 4 seconds (py3)
- input: array.integer a
If a[i] = -1, then the ith position is occupied by a tree.
Otherwise a[i] is the height of a person standing in the ith position.
- guaranteed constraints:
1 ≤ a.length ≤ 1000,
-1 ≤ a[i] ≤ 1000.
- output: array.integer
Sorted array a with all the trees untouched.
"""


def sort_by_height(a):
    swap = True
    while swap:
        swap = False
        for i in range(len(a) - 1):
            if a[i] > a[i + 1] != -1:
                a[i], a[i + 1] = a[i + 1], a[i]
                swap = True
    return a


if __name__ == '__main__':
    row = [-1, 150, 190, 170, -1, -1, 160, 180]
    print(sort_by_height(row))
