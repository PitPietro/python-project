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
    common = [min(s1.count(i), s2.count(i)) for i in set(s1)]
    return sum(common)


def common_character_count_v2(s1, s2):
    count = 0
    commons = set(s1) & set(s2)
    for i in commons:
        count += min(s1.count(i), s2.count(i))
    return count


if __name__ == '__main__':
    a = "aabcc"
    b = "adcaa"
    print(common_character_count(a, b))
    print(common_character_count_v2(a, b))
