#!/usr/bin/python3

def safe_print_division(a, b):
    """divides 2 integers and prints the result
    Args:
    a: int 1
    b: int 2

    Return:
    result of division (success) or None (fail)
    """
    result = 0
    try:
        result = a / b

    except ZeroDivisionError:
        result = None

    finally:
        print("Inside result: {}".format(result))
        return result


# a = 12
# b = 2
# result = safe_print_division(a, b)
# print("{:d} / {:d} = {}".format(a, b, result))

# a = 12
# b = 0
# result = safe_print_division(a, b)
# print("{:d} / {:d} = {}".format(a, b, result))
