#!/usr/bin/python3

def print_square(size):
    """prints a square with the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    # might not need this
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    i = 0
    while(i < size):
        print("#" * size)
        i = i + 1

print_square(9223372036854775807 * 2)
