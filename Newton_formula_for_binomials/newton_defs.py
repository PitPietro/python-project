from binomial_coefficient.binomial_coefficient_defs import binomial_coefficient_int


def newton_formula(a: int, b: int, n: int, k: int) -> str:
    summation = n * (n + 1) // 2
    binomial = binomial_coefficient_int(n, k)

    s = "({} + {})^{} = {} * {} * {}^{} {}^{}"
    return s.format(a, b, n, summation, binomial, a, n - k, b, k)


if __name__ == '__main__':
    print(newton_formula(3, 4, 5, 4))


# def summation(n: int) -> int:
#     k = 0
#     for x in range(n+1):
#         k += x
#     return k
