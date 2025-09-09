#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """replaces or adds key/value in a dictionary
    Args:
    a_dictionary: original dictionary
    key: key to add (if doesn't exist) or replace its value (if exists)
    value: value to replace/add at key in dictionary

    Return: updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
