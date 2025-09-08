#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """adds 2 tuples"""
    # convert tuples to lists to modify, pad with 0s
    new_list_a = list(tuple_a) + [0, 0]
    new_list_b = list(tuple_b) + [0, 0]

    # slice the first 2 elements in each list
    new_list_a = new_list_a[:2]
    new_list_b = new_list_b[:2]

    # perform addition
    a = new_list_a[0] + new_list_b[0]
    b = new_list_a[1] + new_list_b[1]

    # create and return new tuple with correct values
    new_tuple = (a, b)
    return new_tuple


# tuple_a = (1, 89)
# tuple_b = (88, 11)
# new_tuple = add_tuple(tuple_a, tuple_b)
# print(new_tuple)
# print(add_tuple(tuple_a, (1, )))
