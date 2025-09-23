#!/usr/bin/python3
"""
This module provides the add_attribute function.
"""


def add_attribute(obj, name, value):
    """
    function that adds a new attribute to an object if possible.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
