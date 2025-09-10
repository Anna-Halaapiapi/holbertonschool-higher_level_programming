#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """prints the first x items of a list (ints only)
    Args:
    my_list: original list
    x = number of elements to print

    Return:
    actual number of ints printed
    """
    i = 0
    n = 0
    while (i < x):
        try:
            print("{:d}".format(my_list[i]), end='')
        # except IndexError:
        #     break
        except ValueError:
            i = i + 1
            continue
        except TypeError:
            i = i + 1
            continue
        i = i + 1
        n = n + 1

    print()
    return n
