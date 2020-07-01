from python_structure.data_structures.stacks_queues.stack import Stack
"""
> Task
Write a function that reverses characters in (possibly nested) parentheses in the input string.
Input strings will always be well-formed with matching ()s.

> Example
For input_string = "(bar)", the output should be "rab";
For input_string = "foo(bar)baz", the output should be "foorabbaz";
For input_string = "foo(bar)baz(blim)", the output should be "foorabbazmilb";
For input_string = "foo(bar(baz))blim", the output should be "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".

> Input/Output
- execution time limit: 4 seconds (py3)
- input: string input_string
A string consisting of lowercase English letters and the characters ( and ).
It is guaranteed that all parentheses in input_string form a regular bracket sequence.
- guaranteed constraints:
0 ≤ inputString.length ≤ 50.
- output: string
Return input_string, with all the characters that were in parentheses reversed.
"""


def reverse(string):
    stack = Stack()
    for i in string:
        stack.push(i)

    reversed_s = ""
    for i in range(stack.size()):
        reversed_s += stack.pop()

    return reversed_s


def reverse_in_parentheses(input_string):
    normal_s = ""
    rev_s = ""
    strings = list()
    par_num = 0
    max_num = 0
    list_value = list(list())
    for i, s in enumerate(input_string):
        if s == "(":
            par_num += 1
            max_num += 1
        elif s == ")":
            par_num -= 1
        list_value.append([par_num, s])
        print("i: {}| s: {}| par_num: {}|  list_value: {}".format(i, s, par_num, list_value))
    for k in range(max_num + 1):
        strings.append(list())
        print("k: {}| max: {}| strings: {}".format(k, max_num, strings))

    for i, j in enumerate(list_value):
        strings[j[0]].append(j[1])
        print("i: {}| j: {}| j[0]: {}| j[1]: {}| strings: {}".format(i, j, j[0], j[1], strings))
    return normal_s


def rev(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
            print("start: {}".format(start))
        if s[i] == ")":
            end = i
            print("end: {}".format(end))
            return rev(s[:start] + s[start + 1:end][::-1] + s[end + 1:])
    return s


# props to vanpet90 for his genious idea to use eval in the previous version of this task
def reverse_in_parentheses_v2(s):
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')


def test_enumerate(string_to_e):
    for i, s in enumerate(string_to_e):
        print("i: {}| s: {}| string: {}".format(i, s, string_to_e))


if __name__ == '__main__':
    test_1 = "(bar)"
    test_2 = "foo(bar)baz"
    test_3 = "foo(bar)baz(blim)"
    test_4 = "foo(bar(baz))blim"

    # test_enumerate("abcde")

    print(rev(test_1))
    print(rev(test_2))
    print(rev(test_3))
    print(rev(test_4))
