#!/usr/bin/python3

def fizzbuzz():
    """prints numbers 1 - 100.
    for multiples of 3 - prints Fizz.
    for multiples of 5 - prints Buzz.
    for multiples of 3 & 5 - prints Fizz Buzz."""
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz ", end='')
        elif (i % 3 == 0):
            print("Fizz ", end='')
        elif (i % 5 == 0):
            print("Buzz ", end='')
        else:
            print("{} ".format(i), end='')
