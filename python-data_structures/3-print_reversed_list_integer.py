#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """print all ints in list in reverse order"""
    for val in reversed(my_list):
        print("{:d}".format(val))

    # my_list.reverse()

    # for value in my_list:
    #     print("{:d}".format(value))

# my_list = [1, 2, 3, 4, 5]
# print_reversed_list_integer(my_list)
