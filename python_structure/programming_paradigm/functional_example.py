import random


def increment(a):
    return a + 1


if __name__ == '__main__':
    random_n = random.randint(0, 100)
    incremented_n = increment(random_n)
    print("{} incremented by 1 gives {}".format(random_n, incremented_n))
