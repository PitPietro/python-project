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
    for i in s1:
        for j in s2:
            if i == j:
                num += 1
                break
            print("i: {}\tj: {}\tnum: {}".format(i, j, num))
    return num


if __name__ == '__main__':
    a = "aabcc"
    b = "adcaa"
    r = common_character_count(a, b)
    print(r)
