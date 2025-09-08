#!/usr/bin/python3

def no_c(my_string):
    """removes all instances of c and C in a string.
    Args:
    my_string: original string to replace.
    Return:
    updated string without any occurances of 'c' or 'C'
    """
    new_string = ""

    for char in my_string:
        if char != 'c' and char != 'C':
            new_string = new_string + char

    return new_string

# print(no_c("Best School"))
# print(no_c("Chicago"))
# print(no_c("C is fun!"))
