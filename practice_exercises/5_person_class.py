#!/usr/bin/python3
"""
This module provides the person class.
"""

class Person:
    """
    This class defines a Person.
    """
    # counts how many Person objects are created
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    # name - getter
    @property
    def name(self):
        return self.__name

    # name- setter
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self.__name = value

    # age = getter
    @property
    def age(self):
        return self.__age

    # age - setter
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise  TypeError("age must be a positive integer")
        self.__age = value

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    @classmethod
    def get_population(cls):
        print(f"Current Population: {cls.population}")

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

    def __str__(self):
        return f"{self.name}, {self.age} years old"

p1 = Person("Bambi", 2)
p2 = Person("Billy", 5)

p1.say_hello()
p2.say_hello()
Person.get_population()
print(repr(p1))
print(repr(p2))

print(p1)
print(p2)
