#!/usr/bin/python3

def islower(c):
    """Checks for lowercase letter. Returns True for lowercase else returns False"""
    result = ord(c)

    if (result >= 97) and (result <= 122):
        return True
    else:
        return False
