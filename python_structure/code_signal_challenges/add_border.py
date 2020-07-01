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
        if i == 0 or i == len(picture) + 1:
            res_list.append("*" * border)
        else:
            tmp_string = "*"
            tmp_string += picture[i - 1]
            tmp_string += "*"
            res_list.append(tmp_string)
            print("tmp string: {}".format(tmp_string))
        print("result string: {}| i: {}".format(res_list, i))
    return res_list


def add_border_v2(picture):
    borders = len(picture[0]) + 2
    return ["*" * borders] + [x.center(borders, "*") for x in picture] + ["*" * borders]


def add_border_v3(picture):
    result = ['*' * (len(picture[0]) + 2)]
    for i in picture:
        result.append('*' + i + '*')
    result.append(result[0])
    return result


if __name__ == '__main__':
    test_1 = ["abc", "ded"]
    test_2 = ["a"]
    test_3 = ["aa", "**", "zz"]
    test_4 = ["abcde", "fghij", "klmno", "pqrst", "uvwxy"]
    test_5 = ["wzy**"]

    print(add_border(test_1))
    # print(add_border(test_2))
    # print(add_border(test_3))
    # print(add_border(test_4))
    # print(add_border(test_5))
