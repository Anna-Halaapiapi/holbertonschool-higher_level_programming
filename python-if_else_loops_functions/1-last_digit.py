#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    posnumber = number * -1
    lastdigit = (posnumber % 10) * -1

elif number >= 0:
    posnumber = number
    lastdigit = posnumber % 10

if lastdigit > 5:
    statement = "and is greater than 5"
elif lastdigit == 0:
    statement = "and is 0"
else:
    statement = "and is less than 6 and not 0"

print(f"Last digit of {number} is {lastdigit} {statement}")
