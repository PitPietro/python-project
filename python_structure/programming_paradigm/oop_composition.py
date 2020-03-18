class Dog:
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
