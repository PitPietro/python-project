def swap(a, b):
    print('a: {}\t b: {}'.format(a, b))
    a, b = b, a
    print('a: {}\t b: {}'.format(a, b))


"""
Please Note:
The values are not saved because the variables are not global and the function has to return.

"""


def multiple_assignment(a, b, c, a_value, b_value, c_value):
    a, b, c, = a_value, b_value, c_value
    print('a: {}\b: {}\tc: {}'.format(a, b, c))


if __name__ == '__main__':
    swap(14, 3)
    alpha = 654
    beta = 54
    circle = 78
    print('a: {}\b: {}\tc: {}'.format(alpha, beta, circle))
    multiple_assignment(alpha, beta, circle, 1, 2, 3)
