from factorial_function.factorial_defs import get_factorial_iterative
from factorial_function.factorial_defs import factorial_recursive

import sys
sys.setrecursionlimit(5000)


def binomial_coefficient_str(n: int, k: int) -> str:
    if 0 < k <= n:
        num = get_factorial_iterative(n)
        den = factorial_recursive(k) * factorial_recursive(n - k)
        result = num/den
        s = "\nn = {}\nk = {}\nThe binomial coefficient of {} and {} is {} / {} = {}"
        return s.format(n, k, n, k, num, den, result)
    else:
        return "\nimpossible"


def binomial_coefficient_int(n: int, k: int) -> int:
    if 0 < k <= n:
        num = get_factorial_iterative(n)
        den = factorial_recursive(k) * factorial_recursive(n - k)
        return num/den
    else:
        return 0


if __name__ == '__main__':
    print("Binomial coefficient:")
    n_main = 7
    k_main = 3

    print(binomial_coefficient_str(7, 5))
    print(binomial_coefficient_str(1, 3))
    s_main = "\nn = {}\nk = {}\nThe binomial coefficient is {}"
    print(s_main.format(n_main, k_main, binomial_coefficient_int(n_main, k_main)))

