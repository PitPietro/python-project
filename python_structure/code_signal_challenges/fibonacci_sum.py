"""
> Task
For a given integer n, return the shortest possible list of distinct
Fibonacci numbers that sum up to n, sorted in ascending order.

> Example
For n = 20, the output should be [2, 5, 13].

> Input/Output
- execution time limit: 4 seconds (py3)
- input: integer n
- guaranteed constraints:
20 ≤ n ≤ 6000.
- output: array.integer
"""


def fibonacci_sum(n):
    fib = []
    fib0 = 1
    fib1 = 1
    fib.append(fib1)
    while fib1 < n:
        fib2 = fib1 + fib0
        fib.append(fib2)
        fib0 = fib1
        fib1 = fib2

    ans = []
    for i in range(len(fib) - 1, -1, -1):
        if n >= fib[i]:
            n -= fib[i]
            ans.append(fib[i])

    return list(reversed(ans))


if __name__ == '__main__':
    print(fibonacci_sum(20))
    print(fibonacci_sum(21))
    print(fibonacci_sum(33))
