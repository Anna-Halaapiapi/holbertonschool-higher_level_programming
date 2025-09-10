#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ prints x elements of a list
    Args:
    my_list: list of items to print
    x: number of items to print

    Return:
    number of items printed
    """
    # try print x items on list
    i = 0
    n = 0
    while (i < x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except TypeError:
            break
        except IndexError:
            break
        i = i + 1
        n = n + 1

    print()  # print newline
    return n
