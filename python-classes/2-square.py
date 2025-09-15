#!/usr/bin/python3
"""
This module provides the Square class.
"""


class Square:
    """
    The Square class has a private attribute, size.
    TypeError is raised if size is not an integer.
    ValueError is raised if size is less than 0.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
