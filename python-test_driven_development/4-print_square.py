#!/usr/bin/python3
"""
This module provides the print_square function.
This function takes an int for size argument, and
prints a square of '#' of the given size.
TypeError is raised if size is not int.
ValueError is raised if size is less than 0.
"""


def print_square(size):
    """prints a square with the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    i = 0
    while (i < size):
        print("#" * size)
        i = i + 1
