#!/usr/bin/python3
"""
This module provides the BaseGeometry and Rectangle classes.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class defines a Square and inherits from Rectangle.
    """
    def __init__(self, size):
        super().__init__(size, size)
        # size validated in Rectangle -> Base Geometry
        self.__size = size

    def area(self):
        return super().area()
