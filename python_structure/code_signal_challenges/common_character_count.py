"""
> Task
Given two strings, find the number of common characters between them.

> Example
For s1 = "aabcc" and s2 = "adcaa", the output should be 3.
Strings have 3 common characters - 2 "a"s and 1 "c".

> Input/Output
- execution time limit: 4 seconds (py3)
- input: string s1 & string s2
A string consisting of lowercase English letters.
- guaranteed constraints:
1 ≤ s1.length < 15.
1 ≤ s2.length < 15.
- output: integer
"""


def common_character_count(s1, s2):
    num = 0
    my_list = []
    str_l = len(s1)
    for i in s1:
        my_list.append(i)
        print("i: {}".format(i))
    print("list: {}".format(my_list))
    for j in s2:
        my_list.append(j)
        print("j: {}".format(j))
    print("list: {}".format(my_list))

    for k in range(len(my_list) - str_l):
        if my_list[k] == my_list[k + str_l]:
            num += 1
        print("k: {}\t{} -- {}\t{}".format(k, my_list[k], my_list[k + 1], num))
    return num


if __name__ == '__main__':
    a = "aabcc"
    b = "adcaa"
    r = common_character_count(a, b)
    print(r)
