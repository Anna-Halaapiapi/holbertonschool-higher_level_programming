#!/usr/bin/python3

def uppercase(str):
    """Prints a string in uppercase"""

    for i in range(len(str)):
        # change letter to its ASCII equiv.
        letter = (ord(str[i]))

        # check if letter is non lower case
        if (letter <= 96) and (letter >= 123):
            # convert from ASCII to letter
            chr(letter)
            # print letter
            print("{}".format(letter))
            # skip rest of loop to move to next letter
            continue

        # if lowercase letter, get ASCII equiv. of its upp. case
        letter = letter - 32
        # change from ASCII to letter & print
        print("{}".format(chr(letter)))
