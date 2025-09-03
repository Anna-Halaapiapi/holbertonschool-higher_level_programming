#!/usr/bin/python3

def print_last_digit(number):
    """prints last digit of number. returns last digit"""
    if number < 0:
        pos_number = number * -1
        last_digit = (pos_number % 10)

    elif number >= 0:
        last_digit = number % 10
    
    print("{}".format(last_digit), end='')
    return(last_digit)
