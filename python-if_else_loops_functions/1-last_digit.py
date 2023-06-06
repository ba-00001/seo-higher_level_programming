#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
prefix = "Last digit of"
suffix = "and is"

if last_digit > 5:
    print(f"{prefix} {number} {suffix} greater than 5 \n")
elif last_digit == 0:
    print(f"{prefix} {number} {suffix} 0\n")
else:
    print(f"{prefix} {number} {suffix} less than 6 and not 0\n")
