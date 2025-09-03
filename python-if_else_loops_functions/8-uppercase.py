#!/usr/bin/python3

def uppercase(str):
    """Prints a string in uppercase"""

    for i in range(len(str)):
        letter = (ord(str[i]))

        if (letter <= 96) and (letter >= 123):
            chr(letter)
            print("{}".format(letter))
            continue

        letter = letter - 32
        print("{}".format(chr(letter)))
