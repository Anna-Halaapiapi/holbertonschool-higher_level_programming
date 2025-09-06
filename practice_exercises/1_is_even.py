#!/usr/bin/python3

def is_even(n):
    """return True if n is even, else returns False"""
    if (n % 2 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    from sys import argv, exit
    if (len(argv) != 2):
        print("Error: Usage is ./1_is_even <n>")
        exit(1)

    n = int(argv[1])

    print(is_even(n))
