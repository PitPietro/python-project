"""
> Task
Given the string, check if it is a palindrome.

> Example
For inputString = "aabaa", the output should be true;
For inputString = "abac", the output should be false;
For inputString = "a", the output should be true.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: string inputString
A non-empty string consisting of lowercase characters.
- guaranteed constraints:
1 ≤ inputString.length ≤ 105.
- output: boolean
true if inputString is a palindrome, false otherwise.
"""


def check_palindrome(input_string):
    input_string = input_string.lower()
    return input_string[::-1] == input_string


if __name__ == '__main__':
    test_1 = "aabaa"
    test_2 = "abac"
    test_3 = "a"

    print(check_palindrome(test_1))
    print(check_palindrome(test_2))
    print(check_palindrome(test_3))
