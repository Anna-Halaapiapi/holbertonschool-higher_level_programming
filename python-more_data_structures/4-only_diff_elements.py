#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """returns all elements present in only one set"""
    result = set_1 ^ set_2
    return result


# set_1 = { "Python", "C", "Javascript" }
# set_2 = { "Bash", "C", "Ruby", "Perl" }
# od_set = only_diff_elements(set_1, set_2)
# print(sorted(list(od_set)))
