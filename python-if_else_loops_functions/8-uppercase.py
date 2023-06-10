#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            upper_char = chr(ord(char) - 32)
        else:
            upper_char = char
        print(upper_char, end='')
    print()





"""
           8. To uppercase
mandatory
Write a function that prints a string in uppercase followed by a new line.

Prototype: def uppercase(str):
You can only use no more than 2 print functions with string format
You can only use one loop in your code
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()
Tips: ord()
You don’t need to understand __import__


"""

"""
        We iterate over each character in the string using a loop.
For each character, we check if its ASCII value falls within the lowercase range (97 to 122).
If the character is lowercase, we convert it to uppercase by subtracting 32 from its ASCII value and then converting it back to a character using chr().
If the character is not lowercase, we keep it as it is.
We use the print() function with the end='' argument to print each character without a newline.
Finally, we use another print() function without any arguments to print a newline after printing the uppercase string.

"""