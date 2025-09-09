#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """returns a list with all values multiplied by a number.
    Args:
    my_list: the original list
    number: number to multiply values in list with

    Return:
    new list with updated values
    """
    return list(map(lambda x: x * number, my_list))


# my_list = [1, 2, 3, 4, 6]
# new_list = multiply_list_map(my_list, 4)
# print(new_list)
# print(my_list)
