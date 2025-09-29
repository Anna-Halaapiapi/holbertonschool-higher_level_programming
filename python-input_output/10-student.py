#!/usr/bin/python3
"""
This module provides the Student class.
"""


class Student:
    """
    This class defines a Student.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance.
        """
        # return all attributes
        if attrs is None:
            return self.__dict__

        # return specified attributes
        else:
            new_dict = {}
            if len(attrs) == 0:
                return new_dict

            for a in attrs:
                if a in self.__dict__:
                    new_dict[a] = self.__dict__[a]
            return new_dict
