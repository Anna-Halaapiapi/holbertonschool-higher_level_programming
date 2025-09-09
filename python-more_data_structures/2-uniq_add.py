#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds  all unique integers in a list
    (only once for each integer)

    Args:
    my_list: original list

    Return:
    sum of all unique ints in list
    """
    # set only stores unique values
    unique_list = list(set(my_list))
    result = sum(unique_list)
    return result


# my_list = [1, 2, 3, 1, 4, 2, 5]
# result = uniq_add(my_list)
# print("Result: {:d}".format(result))
