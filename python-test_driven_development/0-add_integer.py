#!/usr/bin/python3
"""
This module provides the add_integer function that adds two integers.

The function accepts integers or floats, and will convert any floats to ints.
Any other data types passed to the function will raise a TypeError.
"""
def add_integer(a, b=98):
    """adds two ints.
    Args:
    a = first int
    b = second int

    Return:
    result of addition (pass) or nothing (fail)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
        return

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
        return

    return int(a) + int(b)
