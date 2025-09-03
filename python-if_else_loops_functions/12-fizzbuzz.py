#!/usr/bin/python3

def fizzbuzz():
    """prints numbers 1 - 100.
    for multiples of 3 - prints Fizz.
    for multiples of 5 - prints Buzz.
    for multiples of 3 & 5 - prints Fizz Buzz."""
    for i in range(1, 100):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz ")
        elif (i % 3 == 0):
            print("Fizz ")
        elif (i % 5 == 0):
            print("Buzz ")
        else:
            print("{} ".format(i))

    print("Buzz")
