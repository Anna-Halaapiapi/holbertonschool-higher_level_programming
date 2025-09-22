#!/usr/bin/python3
"""
This module provides the inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    returns True if obj is instance of any subclass of a_class
    (but not if obj is an instance of a_class)
    else returns False.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
