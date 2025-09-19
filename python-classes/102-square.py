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
        self.size = size

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
        """
        calculates and returns area of square
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """
        defines behaviour for == operator.
        Args:
        self: first object to compare
        other: second object to compare
        returns True if self is equal to other, else returns False.
        """
        return self.size == other.size
    
    def __ne__(self, other):
        """
        defines behaviour for != operator.
        Args:
        self: first object to compare
        other: second object to compare
        return True if self not equal to other, else returns False
        """
        return self.size != other.size

    def __gt__(self, other):
        """
        defines behaviour for > operator.
        Args:
        self: first object to compare
        other: second object to compare
        return True if self greater than other, else returns False
        """
        return self.size > other.size
    
    def __ge__(self, other):
        """
        defines behaviour for >= operator.
        Args:
        self: first object to compare
        other: second object to compare
        return True if self greater than/equal to other, else returns False
        """
        return self.size >= other.size
    
    def __lt__(self, other):
        """
        defines behaviour for < operator.
        Args:
        self: first object to compare
        other: second object to compare
        return True if self greater less than other, else returns False
        """
        return self.size < other.size
    
    def __le__(self, other):
        """
        defines behaviour for <= operator.
        Args:
        self: first object to compare
        other: second object to compare
        return True if self greater less than/equal to other, else returns False
        """
        return self.size <= other.size
