#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    statement = "is negative"
elif number == 0:
    statement = "is zero"
else:
    statement = "is positive"
print(f"{number} {statement}")
