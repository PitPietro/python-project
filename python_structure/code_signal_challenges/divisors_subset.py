"""
> Task
Given an array of integers subset and an integer n, find the number
of integers between 1 and n, inclusive, whose set of divisors
contains subset as a subset.

> Example

For subset = [2, 3] and n = 13, the output should be 2.
These integers are 6 and 12.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: array.integer subset
An array of positive integers.
- guaranteed constraints:
1 ≤ subset.length ≤ 5,
1 ≤ subset[i] ≤ 15.
- input: integer n
A positive integer.
- guaranteed constraints:
10 ≤ n ≤ 150.
- output] integer
"""


def divisors_subset(subset, n):
    res = 0
    for i in range(1, n + 1):
        correct = True
        for j in range(len(subset)):
            if i % subset[j] != 0:
                correct = False
        if correct:
            res += 1
    return res


if __name__ == '__main__':
    subset_1 = [2, 3]
    n_1 = 13
    subset_2 = [1]
    n_2 = 62
    subset_3 = [12, 2, 4, 6]
    n_3 = 143

    print(divisors_subset(subset_1, n_1))
    print(divisors_subset(subset_2, n_2))
    print(divisors_subset(subset_3, n_3))
