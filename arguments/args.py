"""
*args
A list of elements 
"""


def multiply(*args):
    result = 1
    for element in args:
        result *= element
    return result


if __name__ == '__main__':
    print(multiply(2, 4, 5, 6, 7))
