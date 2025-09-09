#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """ prints a dictionary by ordered keys"""
    # returns list
    key_sorted = sorted(a_dictionary.items())
    # convert back to dict
    sorted_dict = dict(key_sorted)
    for key, value in sorted_dict.items():
        print("{}: {}".format(key, value))


# a_dictionary = { 'language': "C", 'Number': 89, 'track':
    # "Low level", 'ids': [1, 2, 3] }
# print_sorted_dictionary(a_dictionary)
