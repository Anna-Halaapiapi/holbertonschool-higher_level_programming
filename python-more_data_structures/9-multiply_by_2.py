#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values
    multiplied by 2

    Args:
    a_dictionary: original dictionary

    Return:
    updated dictionary
    """
    new_dict = a_dictionary.copy()

    for key in a_dictionary:
        new_dict[key] = a_dictionary[key] * 2

    return new_dict


# a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
# new_dict = multiply_by_2(a_dictionary)
# print(a_dictionary)
# print(new_dict)
