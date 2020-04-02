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


def reverse_in_parentheses(input_string):
    pass


if __name__ == '__main__':
    test_1 = "(bar)"
    test_2 = "foo(bar)baz"
    test_3 = "foo(bar)baz(blim)"
    test_4 = "foo(bar(baz))blim"

    print(reverse_in_parentheses(test_1))
    print(reverse_in_parentheses(test_2))
    print(reverse_in_parentheses(test_3))
    print(reverse_in_parentheses(test_4))
