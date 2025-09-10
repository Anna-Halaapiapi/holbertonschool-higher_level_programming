#!/usr/bin/python3

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
