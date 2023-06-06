#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit)
    return last_digit




"""
          9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important
mandatory
Write a function that prints the last digit of a number.

Prototype: def print_last_digit(number):
Returns the value of the last digit
You are not allowed to import any module
You don’t need to understand __import__

guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/env python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

guillaume@ubuntu:~/$ ./9-main.py
8044
guillaume@ubuntu:~/$ 


"""

"""
        We use the modulus operator % to get the remainder when the absolute value of the number 
        is divided by 10. This gives us the last digit of the number.
The abs() function is used to ensure that we always work with 
the positive value of the number, regardless of whether it is positive or negative.
We print the last digit using the print() function.
Finally, we return the last digit from the function.

"""