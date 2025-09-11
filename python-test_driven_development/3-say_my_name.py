#!/usr/bin/python3
"""
This module provides the say_my_name function.
The function takes strings as arguments, first name
and last name.
TypeError is returned if arguments passed aren't strings.
"""


def say_my_name(first_name, last_name=""):
    """prints a string followed by first and last name args"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is ", end='')
    print("{} {}".format(first_name, last_name))
