"""
https://app.codesignal.com/tournaments/DC5rpkx6XZeavRtdC/D

> Task
Find the sum of all divisors of a given integer.

> Example
For n = 12, the output should be  28.
Explanation: 1 + 2 + 3 + 4 + 6 + 12 = 28.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: integer n
A positive integer.
- guaranteed constraints:
1 ≤ n ≤ 5 · 108.
- output: integer
"""


def sum_of_divisors(n):
    s = 0
    if n == 0:
        return 0
    for i in range(1, n + 1):
        if n % i == 0:
            s += i
    return s


if __name__ == '__main__':
    print(sum_of_divisors(12))
