#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """deletes a key in a dictionary
    Args:
    a_dictionary: original dictionary
    key: key to delete in dictionary

    Return: original dictionary (key doesn't exist) or
    updated dictionary.
    """
    # only delete key if exists
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary


# a_dictionary = { 'language': "C", 'Number': 89,
#  'track': "Low", 'ids': [1, 2, 3] }
# print(a_dictionary)
# new_dict = simple_delete(a_dictionary, 'hello')
# print(a_dictionary)
