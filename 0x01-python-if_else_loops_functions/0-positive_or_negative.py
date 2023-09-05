#!/usr/bin/python3
import random

number = random.randint(-10, 10)
if number > 0:
    output = "is positive"
elif number == 0:
    output = "is zero"
else:
    output = "is negative"
print(f"{number} {output}")
