"""
https://www.hackerrank.com/challenges/alphabet-rangoli/problem
"""
from string import ascii_lowercase as ascii_l


def print_rangoli(size):
    size = size - 1
    alpha = list(ascii_l)
    main_s = ''
    for i in range(size, -1, -1):
        tmp = alpha[i] + '-'
        main_s += tmp
        print(main_s)
    print('|||||||')
    main_s = main_s[:-1]
    print(main_s)
    for i in range(1, size + 1):
        tmp = '-' + alpha[i]
        main_s += tmp
        print(main_s)
    print('|||||||')
    print(main_s)
    # print(alpha[size])


if __name__ == '__main__':
    # n = int(input())
    n = 5
    print_rangoli(n)
