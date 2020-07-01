"""
> Task
Given an array of strings, return another array containing all of its longest strings.

> Example
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be ["aba", "vcd", "aba"].

> Input/Output
- execution time limit: 4 seconds (py3)
- input: array.string inputArray
A non-empty array.
- guaranteed constraints:
1 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 10.
- output: array.string
Array of the longest strings, stored in the same order as in the inputArray.
"""


def all_longest_strings(input_array):
    max_len = 0
    longest = []
    for i in input_array:
        if len(i) > max_len:
            max_len = len(i)
    for j in input_array:
        if len(j) == max_len:
            longest.append(j)
    return longest


def all_longest_strings_v2(input_array):
    m = max(len(s) for s in input_array)
    r = [s for s in input_array if len(s) == m]
    return r


if __name__ == '__main__':
    string_1 = ["aba", "aa", "ad", "vcd", "aba"]
    print(all_longest_strings(string_1))
    print(all_longest_strings_v2(string_1))


