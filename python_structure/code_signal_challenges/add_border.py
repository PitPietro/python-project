"""
> Task
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

> Example
For picture = ["abc", "ded"] the output should be ["*****", "*abc*", "*ded*", "*****"]

> Input/Output
- execution time limit: 4 seconds (py3)
- input: array.string picture
A non-empty array of non-empty equal-length strings.
- guaranteed constraints:
1 ≤ picture.length ≤ 100,
1 ≤ picture[i].length ≤ 100.
- output: array.string
The same matrix of characters, framed with a border of asterisks of width 1.
"""


def add_border(picture):
    border = len(picture[0]) + 2
    print("border len: {}".format(border))
    print("picture len: {}".format(len(picture)))
    res_list = []
    for i in range(len(picture) + 2):
        res_list.append([])
        print("result list: {}".format(res_list))

    for i, j in enumerate(res_list):
        if i == 0 or i == len(res_list) - 1:
            for k in range(border):
                j.append("*")
        else:
            j.append("*")
            for k in picture[i - 1]:
                j.append(k)
            j.append("*")
        print("i: {}| j: {}".format(i, j))
    return res_list


if __name__ == '__main__':
    test_1 = ["abc", "ded"]
    test_2 = ["a"]
    test_3 = ["aa", "**", "zz"]
    test_4 = ["abcde", "fghij", "klmno", "pqrst", "uvwxy"]
    test_5 = ["wzy**"]

    print(add_border(test_1))
    print(add_border(test_2))
    print(add_border(test_3))
    print(add_border(test_4))
    print(add_border(test_5))
