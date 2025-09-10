#!/usr/bin/python3

def raise_exception_msg(message=""):
    """raises a name exception with a message
    Args:
    message: message to return

    Return:
    message
    """

    raise NameError(message)


# try:
#     raise_exception_msg("C is fun")
# except NameError as ne:
#     print(ne)
