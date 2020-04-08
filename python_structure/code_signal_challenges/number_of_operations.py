"""
https://app.codesignal.com/tournaments/DC5rpkx6XZeavRtdC/C

> Task
For a pair of two positive integers a and b consider the
following operation: if one of the integers is divisible
by the other - replace this integer with the division
result of the two. This operation is applied sequentially
until it stops working. Return the number of times the
operation is applied. It is guaranteed that the answer
is a finite number.

> Example
For a = 432 and b = 72, the output should be 4.
For (a, b) = (432, 72) there will be 4 such operations:
(432, 72) -> (6, 72) -> (6, 12) -> (6, 2) -> (3, 2).

> Input/Output
- execution time limit: 4 seconds (py3)
- input: integer a & integer b
- guaranteed constraints:
2 ≤ a ≤ 108.
2 ≤ b ≤ 108.
- output: integer
"""


def number_of_operations(a, b):
    pass


if __name__ == '__main__':
    # 4
    print(number_of_operations(432, 72))
    # 1
    print(number_of_operations(7, 14))
