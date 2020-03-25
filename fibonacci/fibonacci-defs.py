# Fibonacci tool
# This script only works with Python3!

import time


def get_fibonacci_iterative(n: int) -> int:
    """
    Calculate the fibonacci number at position 'n' in an iterative way
    :param n: position number
    :return: position n of Fibonacci series
    """
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b

    return a


def get_fibonacci_iterative_print(n: int):
    """
    Calculate the fibonacci number at position 'n' in an iterative way
    printing the steps
    :param n: position number
    :return: position n of Fibonacci series
    """

    a1 = 0
    a2 = 1

    for i in range(n):
        a1, a2 = a2, a1 + a2
        s = "a: {} \t b: {}"
        print(s.format(a1, a2))

    s1 = "The element n°{} is {}"
    print(s1.format(n, a1))


def get_fibonacci_recursive(n: int) -> int:
    """
    Calculate the fibonacci number at position n recursively
    :param n: position number
    :return: position n of Fibonacci series
    """

    a = 0
    b = 1

    def step(n: int) -> int:
        nonlocal a, b
        if n <= 0:
            return a
        a, b = b, a + b
        return step(n - 1)

    return step(n)


def compare_fibonacci_calculators(n: int) -> None:
    """
    Interactively compare both fibonacci generators
    :param n: position number
    :return: string of the calculated time
    """

    start_i = time.clock()
    result_i = get_fibonacci_iterative(n)
    end_i = time.clock()

    start_r = time.clock()
    result_r = get_fibonacci_recursive(n)
    end_r = time.clock()

    s = "{} calculating {} => {} in {} seconds"
    print(s.format(
        "Iteratively", n, result_i, end_i - start_i
    ))
    print(s.format(
        "Recursively", n, result_r, end_r - start_r
    ))


def fibonacci_list(n):
    """
    Return a list of n Fibonacci element
    :param n: number of list element
    :return: a list
    """
    my_fib = [0, 1]

    if n == 1:
        return [0]
    elif n == 2:
        return my_fib
    elif n <= 0:
        pass
    else:
        for i in range(0, n - 2):
            max_index = len(my_fib)
            element_1 = my_fib[max_index - 2]
            element_2 = my_fib[max_index - 1]
            sum_element = element_1 + element_2
            my_fib.append(sum_element)
        return my_fib


if __name__ == '__main__':
    print(get_fibonacci_iterative(3))
    print(get_fibonacci_recursive(3))
    compare_fibonacci_calculators(3)
    get_fibonacci_iterative_print(3)
    print(fibonacci_list(-4))
