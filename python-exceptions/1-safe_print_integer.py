#!/usr/bin/python3

def safe_print_integer(value):
    """prints an integer with "{:d}".format()
    Args
    value: value to print as int (can be any type)

    Returns
    True (success) or False (fail)
    """

    try:
        print("{:d}".format(value))

    except ValueError:
        return False

    return True


# value = 89
# has_been_print = safe_print_integer(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))

# value = -89
# has_been_print = safe_print_integer(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))

# value = "School"
# has_been_print = safe_print_integer(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))
