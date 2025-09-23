#!/usr/bin/python3
"""
This module provides the BaseGeometry and Rectangle classes.
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


class Rectangle(BaseGeometry):
    """
    This class defines a Rectangle and inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
