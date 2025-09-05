#!/usr/bin/python3

x = 124
y = 91
i = 0
letter = 0

while (i < 26):

    if (i % 2 == 0):  # lowercase
        x = x - 2
        letter = x

    elif (i % 2 != 0):  # uppercase
        y = y - 2
        letter = y

    print("{}".format(chr(letter)), end='')
    i = i + 1
