#!/usr/bin/python3

def add(a, b):
    return (a + b)


def sub(a, b):
    return (a - b)


def mul(a, b):
    return (a * b)


def div(a, b):
    return (a / b)


def simple_calculator():
    """computes calculation of user input and prints to stdout"""
    from sys import argv, exit

    if (len(argv) != 4):  # check for correct number of args
        print("Error: Usage is ./0_simple_calc <a> <operation> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if (argv[2] == '+'):
        print(add(a, b))
    elif (argv[2] == '-'):
        print(sub(a, b))
    elif (argv[2] == '*'):
        print(mul(a, b))
    elif (argv[2] == '/'):
        print(div(a, b))
    else:
        print("Error: Invalid operator")
        exit(1)


if __name__ == "__main__":
    simple_calculator()
