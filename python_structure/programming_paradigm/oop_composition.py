class Dog:
    """
    Classes has two kind of variables:
    1- class variables
    Belong to the object and the object's class.
    They're useful because they can be used to share data between
    all the instances of a
    2- Instance variables
    Belong to objects.
    """
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    pit = Person("Pit", 18)
    pet = Dog("Flower", "poodle", pit)
    print(pet.owner.name)
