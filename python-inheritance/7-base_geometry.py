#!/usr/bin/python3
"""
This module provides the BaseGeometry class.
"""


class BaseGeometry:
    """
    This class defines BaseGeometry.
    """
    def area(self):
        """
        raises an Exception with error message.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value argument
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
