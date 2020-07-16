"""
https://app.codesignal.com/tournaments/WbFPgiiJyqMf9mW2N/C
> Task
Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.

> Example
For n = 6, l = 2, and r = 4, the output should be 2.
These ways are: 2 + 4 = 6 and 3 + 3 = 6.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: integer n & integer l & integer r
Positive integers.
- guaranteed constraints:
5 ≤ n ≤ 25.
2 ≤ l ≤ r.
l ≤ r ≤ 20.
- output: integer
"""
from code_signal_challenges.result_is_correct import is_correct


def count_sum_of_two_representations(n, left, right):
    nums = 0
    for a in range(left, right + 1):
        b = n - a
        if left <= a <= b <= right:
            nums += 1
    return nums


if __name__ == '__main__':
    is_correct(count_sum_of_two_representations(6, 2, 4), 2)
    is_correct(count_sum_of_two_representations(6, 3, 3), 1)
    is_correct(count_sum_of_two_representations(10, 9, 11), 0)
    is_correct(count_sum_of_two_representations(24, 8, 16), 5)
    is_correct(count_sum_of_two_representations(24, 12, 12), 1)


