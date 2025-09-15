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
        # if not isinstance(size, int):
        #     raise TypeError("size must be an integer")
        # if size < 0:
        #     raise ValueError("size must be >= 0")

        self.__size = size

    # getter
    @property
    def size(self):
        return self.__size

    # setter
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        area = self.__size * self.__size
        return area

    def my_print(self):
        if self.__size == 0:
            print()

        else:
            i = 0
            while (i < self.__size):
                print("#" * self.__size)
                i = i + 1
