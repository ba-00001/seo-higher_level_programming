#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
prefix = "Last digit of"
suffix = "is"

if number >= 0:
    sign = ""
else:
    sign = "-"

if last_digit > 5 and number >= 0:
    print(f"{prefix} {number} {suffix} {sign}{last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{prefix} {number} {suffix} {sign}{last_digit} and is 0")
else:
    print(f"{prefix} {number} {suffix} {sign}{last_digit} and is less than 6 and not 0")
