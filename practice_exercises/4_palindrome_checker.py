#!/usr/bin/python3
from sys import argv, exit

def simple_palindrome(str):
    """returns True if str is palindrome, else returns False"""
    """simple version - reverses string and compares against original"""
    string_length = len(str)
    reverse_string = str[::-1]
    if (reverse_string == str):
        return True
    else:
        return False

if __name__ == "__main__":
    if (len(argv) != 2):
        print("Usage Error")
        exit(1)
    s = argv[1]
    print(simple_palindrome(s))
