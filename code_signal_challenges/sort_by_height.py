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
            j = i + 1
            while a[i] == -1:
                i += 1
                if i == len(a):
                    return a
            while a[j] == -1:
                j += 1
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                swap = True
    return a


def sort_by_height_v2(a):
    print("\nunsorted: {}".format(a))
    sorted_l = sorted([i for i in a if i > 0])
    print("sorted: {}".format(sorted_l))
    for n, i in enumerate(a):
        print("n: {}  |  i: {}  |  a[{}] = {}".format(n, i, n, a[n]))
        if i == -1:
            sorted_l.insert(n, i)
        print("sorted: {}".format(sorted_l))
    return sorted_l


def sort_by_height_v3(a):
    sorted_l = [n for n in a if n != -1]
    sorted_l.sort()
    for i in range(len(a)):
        a[i] = sorted_l.pop(0) if a[i] != -1 else a[i]
    return a


if __name__ == '__main__':
    test_1 = [-1, 15, 19, 17, -1, -1, 16, 18]
    test_2 = [-1, -1, -1, -1, -1]
    test_3 = [-1]
    test_4 = [4, 2, 9, 11, 2, 16]
    test_5 = [2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]
    test_6 = [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]

    print("\nPit version (quite wrong)")
    print(sort_by_height(test_1))
    print(sort_by_height(test_2))
    print(sort_by_height(test_3))
    print(sort_by_height(test_4))
    print(sort_by_height(test_5))
    print(sort_by_height(test_6))

    print("\n2nd version:")
    print(sort_by_height_v2(test_1))
    print(sort_by_height_v2(test_2))
    print(sort_by_height_v2(test_3))
    print(sort_by_height_v2(test_4))
    print(sort_by_height_v2(test_5))
    print(sort_by_height_v2(test_6))

    print("\n3rd version")
    print(sort_by_height_v3(test_1))
    print(sort_by_height_v3(test_2))
    print(sort_by_height_v3(test_3))
    print(sort_by_height_v3(test_4))
    print(sort_by_height_v3(test_5))
    print(sort_by_height_v3(test_6))
