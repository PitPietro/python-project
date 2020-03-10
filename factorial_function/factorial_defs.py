# Factorial Function defs

import sys
sys.setrecursionlimit(5000)


def get_factorial_iterative(n: int) -> int:
    result = 1

    for i in range(n):
        if i == 0 or i == 1:
            result *= 1
        else:
            result *= i

    result *= n
    return result


def get_factorial_iterative_print(n: int) -> int:
    print("Number = ", n)
    result = 1

    for i in range(n):
        if i == 0 or i == 1:
            result *= 1
        else:
            result *= i
        s = "partial result: {}\titerator: {}"
        print(s.format(result, i))

    result *= n
    return result


def factorial_recursive(n):
    return 1 if(n <= 1) else n * factorial_recursive(n - 1)


if __name__ == '__main__':
    s_main = "\n{}! is {}"
    number = 25
    print(s_main.format(number, get_factorial_iterative_print(number)))
    print(s_main.format(number, factorial_recursive(number)))