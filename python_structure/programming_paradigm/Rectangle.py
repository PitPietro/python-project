class Rectangle:
    # the corresponding of Java's static
    recs = []

    def __init__(self, vertex_1, vertex_2, vertex_3, vertex_4, width, length):
        self.name = vertex_1 + vertex_2 + vertex_3 + vertex_4
        self.width = width
        self.length = length
        self.recs.append((self.name, self.width, self.length))

    def area(self):
        return self.width * self.length

    def change_size(self, width, length):
        self.width = width
        self.length = length

    def __repr__(self):
        """
        The corresponding of Java's 'toString()' method
        :return: information about the object
        """
        msg = "{}\twidth: {}\tlength: {}".format(self.name, self.width, self.length)
        return msg


if __name__ == '__main__':
    r_one = Rectangle("A", "B", "C", "D", 4, 6)
    r_two = Rectangle("B", "D", "F", "E", 14, 10)
    print(r_one.__repr__())
    print("area: ", r_one.area())
    r_one.change_size(8, 2)
    print(r_one.__repr__())
    print("area: ", r_one.area())
    # print all the rectangles
    print(r_one.recs)
