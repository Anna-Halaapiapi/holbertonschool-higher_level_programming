#!/usr/bin/python3

def no_c(my_string):
    """replaces all instances of c and C in a string with
    an empty string.
    Args:
    my_string: original string to replace.

    Return:
    new string without any occurance of 'c' or 'C'
    """
    new_string = my_string.replace("c" and "C", "")
    return new_string


# print(no_c("Best School"))
# print(no_c("Chicago"))
# print(no_c("C is fun!"))
