#!/usr/bin/python3
from sys import argv, exit

def fibonacci(n):
    """returns nth fibonacci number"""
    i = 2  # index position
    a = 0  # 1st number
    b = 1  # 2nd number
    result = 0

    if (n == 0):
        return 0
    if (n == 1):
        return 1

    while (i <= n):
        result = a + b
        a = b
        b = result
        i = i + 1

    return(result)

if __name__ == "__main__":
    if (len(argv) != 2):
        print("Usage error")
        exit(1)

    n = int(argv[1])

print(fibonacci(n))
