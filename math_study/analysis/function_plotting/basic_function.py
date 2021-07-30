class BasicFunction:
    def __init__(self, a=0., b=0., c=0.):
        """
        a - coefficient of x^2
        b - coefficient of x
        c - known term
        """
        self.a = a
        self.b = b
        self.c = c

    def value_in_x(self, x):
        value = self.a * x ** 2 + self.b * x + self.c
        print('f({}) = {}'.format(x, value))
        return value


if __name__ == '__main__':
    f = BasicFunction(2, 3, 5)
    f.value_in_x(3)
