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
from collections import deque, Counter


def palindrome_rearranging(input_string):
    if check_palindrome(input_string):
        return True
    else:
        for i in range(len(input_string)):
            for j in range(len(input_string)):
                temp_b = input_string
                if i != j:
                    temp_string = temp_b[j]
                    temp_b = temp_b.replace(temp_b[j], temp_b[i])
                    temp_b = temp_b.replace(temp_b[i], temp_string)
                    print("i: {}| j: {}| temp_b: {}| temp_string: {}".format(i, j, temp_b, temp_string))
                    if check_palindrome(temp_b):
                        return True
    return False


def palindrome_from(letters):
    """
    Forms a palindrome by rearranging :letters: if possible,
    throwing a :ValueError: otherwise.
    :param letters: a suitable iterable, usually a string
    :return: a string containing a palindrome
    """
    counter = Counter(letters)
    sides = []
    center = deque()
    for letter, occurrences in counter.items():
        repetitions, odd_count = divmod(occurrences, 2)
        if not odd_count:
            sides.append(letter * repetitions)
            continue
        if center:
            raise ValueError("no palindrome exists for '{}'".format(letters))
        center.append(letter * occurrences)
    center.extendleft(sides)
    center.extend(sides)
    return ''.join(center)


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

    index = 1
    print(index, ") ", palindrome_rearranging(test_1))
    index += 1
    print(index, ") ", palindrome_rearranging(test_2))
    index += 1
    print(index, ") ", palindrome_rearranging(test_3))
    index += 1
    print(index, ") ", palindrome_rearranging(test_4))
    index += 1
    print(index, ") ", palindrome_rearranging(test_5))
    index += 1
    print(index, ") ", palindrome_rearranging(test_6))
    index += 1
    print(index, ") ", palindrome_rearranging(test_7))
    index += 1
    print(index, ") ", palindrome_rearranging(test_8))
    index += 1
    print(index, ") ", palindrome_rearranging(test_9))
    index += 1
    print(index, ") ", palindrome_rearranging(test_10))

    print()
    flag = True
    while flag:
        try:
            word = input('Enter a word: ')
            if word == "flag = false":
                flag = False
            print(palindrome_from(word))
        except ValueError as e:
            print(*e.args)
        except EOFError:
            break
