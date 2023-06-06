#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
prefix = "Last digit of"
suffix = "is"


if number <= 0:
    last_digit = -1 * last_digit
str1 = f"{prefix} {number} {suffix} {last_digit}"
if last_digit > 5 and number >= 0:
    print(str1 + " and is greater than 5")
elif last_digit == 0:
    print(str1 + " and is 0")
else:
    print(str1 + " and is less than 6 and not 0")
