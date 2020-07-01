class Banana:
    def __init__(self, id, w, h):
        """
        '__init__' is a so called magic function
        'self' is used to define an instance variable that belong to an object.
        The instance variables should always be defined inside this method
        :param w: banana's weight
        :param h: banana's height
        """
        self.id = id
        self.weight = w
        self.height = h
        print("Banana created!")


if __name__ == '__main__':
    b_one = Banana(1, 10.2, 45.6)
    b_two = Banana(2, 20.2, 15.6)
    b_three = Banana(3, 14.2, 50.6)

    # print the 1st banana's state
    print(b_one)
    print(b_one.id)
    print(b_one.weight)
    print(b_one.height)
    print("\n")

    # print the 2nd banana's state
    print(b_two)
    print(b_two.id)
    print(b_two.weight)
    print(b_two.height)
    print("\n")

    # print the 3rd banana's state
    print(b_three)
    print(b_three.id)
    print(b_three.weight)
    print(b_three.height)
    print("\n")
