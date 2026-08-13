"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Animal:
    color = "Brown"

    def __init__(self, habitat, food):
        self.habitat = habitat
        self.food = food

    def display_info(self):
        print(f"Habitat: {self.habitat}, Food: {self.food}")


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Dog(Animal):
    sound = "Woof"

    def __init__(self, habitat, food, name, age):
        super().__init__(self, habitat, food)
        self.name = name
        self.age = age

    def set_age(self, age):
        self.age = age

    def display_info(self):
        animal_info = super().display_info()
        print(f"{animal_info}, Name: {self.name}, Age: {self.age}")



# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")
    dog1 = Dog("land", "meat", "Sparky", 8)
    dog2 = Dog("land", "meat", "Rex", 5)
    Dog.sound = "Bark"
    dog1.sound = "Ruff"
    dog1.fur = "long"
    print(dog1.__dict__)
    print(dog2.__dict__)
    dog1.display_info()
    dog2.display_info()



# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")

    coordinates = [
        [1, 2],
        [3, 4]
    ]

    shallow_copy = copy.copy(coordinates)
    deep_copy = copy.deepcopy(coordinates)

    coordinates[0].append(99)

    # The shallow copy is just a pointer reference to the same original list.
    # With a shallow copy, changing the original also changes the copy, because they're the same.
    # The deep copy makes a entirely separate list that can be changed without changing the original.
    print(f"Original: {coordinates}")
    print(f"Shallow copy: {shallow_copy}")
    print(f"Deep copy: {deep_copy}")



# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")

    print("\nTODO: Create and test your child object")

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()