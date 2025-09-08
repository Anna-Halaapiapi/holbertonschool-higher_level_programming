#!/usr/bin/python3

def max_integer(my_list=[]):
    """finds biggest int in list"""
    # if list is empty
    if len(my_list) == 0:
        return None

    # # sort list in descending order
    # # this is more ineffecient than scanning each value as below:

    # my_list.sort(reverse=True)
    # return my_list[0]

    max_value = my_list[0]

    for number in my_list[1:]:
        if number > max_value:
            max_value = number

    return max_value


# my_list = [1, 90, 2, 13, 34, 5, -13, 3]
# max_value = max_integer(my_list)
# print("Max: {}".format(max_value))
