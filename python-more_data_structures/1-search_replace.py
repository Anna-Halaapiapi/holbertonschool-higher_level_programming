#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element with another
    
    Args:
    my_list: original list
    search: the element to replace
    replace: the new element
    
    Return:
    the updated list
    """
    new_list = []

    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)

    return new_list


# my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
# new_list = search_replace(my_list, 2, 89)

# print(new_list)
# print(my_list)
