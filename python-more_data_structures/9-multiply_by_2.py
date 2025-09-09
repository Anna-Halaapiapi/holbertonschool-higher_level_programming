#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values
    multiplied by 2

    Args:
    a_dictionary: original dictionary

    Return:
    updated dictionary
    """
    for key in a_dictionary:
        a_dictionary[key] = a_dictionary[key] * 2

    return a_dictionary


# a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
# print(a_dictionary)
# new_dict = multiply_by_2(a_dictionary)
# print(new_dict)
