#!/usr/bin/python3
"""
This module provides the Rectangle class.
"""


class Rectangle:
    """
    This class defines a Rectangle.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # width - getter
    @property
    def width(self):
        return self.__width

    # height - getter
    @property
    def height(self):
        return self.__height

    # width - setter
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # height - setter
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        hashes = ""
        if self.width == 0 or self.height == 0:
            return hashes
        row = "#" * self.width
        length = self.height - 1
        for i in range(0, length):
            hashes += row
            hashes += "\n"
        hashes += row
        return hashes
