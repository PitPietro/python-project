import time


def print_arrow(n, d):
    for i in range(1, n):
        for j in range(0, i):
            print('-', end='')
            time.sleep(d)
        for k in range(0, i):
            print('*', end='')
            time.sleep(d)
        print()
    for i in range(0, n):
        for j in range(0, n - 1):
            print('+', end='')
            time.sleep(d)
        for k in range(0, n-i):
            print('*', end='')
            time.sleep(d)
        print()


if __name__ == '__main__':
    print_arrow(6, 0.2)
