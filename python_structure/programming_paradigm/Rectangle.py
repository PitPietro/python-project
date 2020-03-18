class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def change_size(self, width, length):
        self.width = width
        self.length = length


if __name__ == '__main__':
    r_one = Rectangle(4, 6)
    print("Area: ", r_one.area())
    r_one.change_size(8, 2)
    print("Area: ", r_one.area())
