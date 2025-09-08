#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element in list at specifc position,
    without modifying the orginal list.
    Args:
    my_list: a list of ints.
    idx: index position of list element to replace.
    element: replacement element.

    Return: new list (success) or original list (fail)
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = my_list.copy()
    new_list[idx] = element

    return new_list


# my_list = [1, 2, 3, 4, 5]
# idx = 3
# new_element = 9
# new_list = new_in_list(my_list, idx, new_element)

# print(new_list)
# print(my_list)
