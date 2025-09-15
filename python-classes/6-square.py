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
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    # size - getter
    @property
    def size(self):
        return self.__size

    # size - setter
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    # position - getter
    @property
    def position(self):
        return self.__position

    # position - setter
    @position.setter
    def position(self, value):
        msg = "position must be a tuple of 2 positive integers"
        if not isinstance(value, tuple):
            raise TypeError(msg)

        if len(value) != 2:
            raise TypeError(msg)

        if not isinstance(value[0], int):
            raise TypeError(msg)

        if not isinstance(value[1], int):
            raise TypeError(msg)

        if value[0] < 0 or value[1] < 0:
            raise TypeError(msg)

        self.__position = value

    def area(self):
        area = self.__size * self.__size
        return area

    def my_print(self):
        if self.__size == 0:
            print()

        else:
            i = 0
            print("\n" * self.__position[1], end='')
            while (i < self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
                i = i + 1
