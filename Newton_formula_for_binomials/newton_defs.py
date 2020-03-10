from binomial_coefficient.binomial_coefficient_defs import binomial_coefficient_int


def newton_formula(a: int, b: int, n: int, k: int) -> str:
    sum = summation(n)
    binomial = binomial_coefficient_int(n, k)

    s = "({} + {})^{} = {} * {} * {}^{} {}^{}"
    return s.format(a, b, n, sum, binomial, a, n-k, b, k)


def summation(n: int) -> int:
    k = 0
    for x in range(n+1):
        k += x
    return k


if __name__ == '__main__':
    print(summation(3))
    print(newton_formula(3, 4, 5, 4))
