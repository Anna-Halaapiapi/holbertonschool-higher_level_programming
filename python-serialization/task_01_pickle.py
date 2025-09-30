#!/usr/bin/python3
"""
This module provides the CustomObject class.
"""

import pickle


class CustomObject:
    """
    defines a CustomObject
    """
    def __init__(self, name, age, is_student):
        if not isinstance(name, str):
            raise TypeError("name provided must be a string")
        self.name = name
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        self.age = age
        if not isinstance(is_student, bool):
            raise TypeError("is student must be a boolean")
        self.is_student = is_student

    def display(self):
        """
        prints object's attributes in format required by task.
        """
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}", end='')

    def serialize(self, filename):
        """
        using pickle, serializes the current instance of the object
        and saves it to the provided filename.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)

        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        using pickle, this function will load and return an instance
        of the CustomObject from the provided filename.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (OSError, pickle.PickleError):
            return None
