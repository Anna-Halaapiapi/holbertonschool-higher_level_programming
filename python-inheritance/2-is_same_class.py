#!/usr/bin/python3
"""
This module provides the is_same_class function.
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class
    otherwise returns False.
    """
    if type(obj) is a_class:
        return True
    return False
