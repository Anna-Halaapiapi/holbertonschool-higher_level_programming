#!/usr/bin/python3
"""
This module provides the MyInt class
"""


class MyInt(int):
    """
    This class defines MyInt and inherits from int.
    """
    def __init__(self, value):
        self.number = value

    # number - getter
    @property
    def number(self):
        return self.__number

    # number - setter
    @number.setter
    def number(self, value):
        if not isinstance(value, int):
            raise TypeError("number must be an integer")
        self.__number = value

    # custonm __eq__ - returns false if self equals other
    def __eq__(self, other):
        return self.__number != other

    # custom __ne__ - returns false if self doesn't equal other
    def __ne__(self, other):
        return self.number == other
