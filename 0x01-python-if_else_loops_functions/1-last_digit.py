#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
last_digit = last_digit if number >= 0 else last_digit * -1
if last_digit > 5:
    sign = "greater than 5"
elif last_digit == 0:
    sign = "0"
elif last_digit < 6 and not 0:
    sign = "less than 6 and not 0"
else:
    sign = ""
print(f"Last digit of {number} is {last_digit} and is {sign}")
