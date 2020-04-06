"""
> Task
Given a string, find out if its characters can be rearranged to form a palindrome.

> Example
For inputString = "aabb", the output should be true.
We can rearrange "aabb" to make "abba", which is a palindrome.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: string inputString
A string consisting of lowercase English letters.
- guaranteed constraints:
1 ≤ inputString.length ≤ 50.
- output: boolean
true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.36
"""
from python_structure.code_signal_challenges.check_palindrome import check_palindrome


def palindrome_rearranging(input_string):
    if check_palindrome(input_string):
        return True


if __name__ == '__main__':
    # true
    test_1 = "aabb"
    # false
    test_2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"
    # true
    test_3 = "abbcabb"
    # true
    test_4 = "zyyzzzzz"
    # true
    test_5 = "z"
    # true
    test_6 = "zaa"
    # false
    test_7 = "abca"
    # false
    test_8 = "abcad"
    # false
    test_9 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbccccaaaaaaaaaaaaa"
    # false
    test_10 = "abdhuierf"

    print(palindrome_rearranging(test_1))
    print(palindrome_rearranging(test_2))
    print(palindrome_rearranging(test_3))
    print(palindrome_rearranging(test_4))
    print(palindrome_rearranging(test_5))
    print(palindrome_rearranging(test_6))
    print(palindrome_rearranging(test_7))
    print(palindrome_rearranging(test_8))
    print(palindrome_rearranging(test_9))
    print(palindrome_rearranging(test_10))
