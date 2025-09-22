#!/usr/bin/python3
"""
This module provides the is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class
    or any subclass derived from a_class.
    Return False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
