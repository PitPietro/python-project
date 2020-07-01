class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        """
        'abs' return the absolute value
        :param other: object of class
        :return: absolute value of the sum
        """
        return abs(self.n + other.n)


if __name__ == '__main__':
    """
    'override' the __add__ method
    """
    x = AlwaysPositive(-20)
    y = AlwaysPositive(10)
    print(x + y)
