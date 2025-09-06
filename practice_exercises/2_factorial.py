#!/usr/bin/python3

import math
from sys import argv, exit

def factorial(n):
    """returns factorial of n"""
    return(math.factorial(n))

if __name__ == "__main__":
    if (len(argv) != 2):
        print("Error: usage is ./2_factorial <n>")
        exit(1)

    n = int(argv[1])

    if n == 0:
        print("1")
        exit(0)

    print(factorial(n))
