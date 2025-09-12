#!/usr/bin/python3
"""
This module provides the text_indentation function.
This function receives a string, and separates lines based on
special characters as the separators.
TypeError will be raised if the text passed to the function is not a string.
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters:
    .
    ?
    :
    Args:
    text: the original text in which to insert new lines
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    spec_char = [":", ".", "?"]
    line = ''

    for char in text:
        line += char
        if char in spec_char:
            print(line.strip())
            print()
            print()
            line = ''

    # print any leftover line(s)
    if len(line.strip()) > 0:
        print(line.strip())
