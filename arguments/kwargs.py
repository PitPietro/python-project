"""
**kwargs
"""


def print_info(**kwargs):
    for key in kwargs:
        print('{}: {}'.format(key, kwargs[key]))


if __name__ == '__main__':
    print_info(name='Mike', lastname='Red', age=22)