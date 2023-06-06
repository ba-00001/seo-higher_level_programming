#!/usr/bin/python3
for num1 in range(10):
    for num2 in range(num1 + 1, 10):
        if num1 < 8:
            print("{:d}{:d}, ".format(num1, num2), end="")
        else:
            print("{:d}{:d}".format(num1, num2))


    """
    6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
mandatory
Write a program that prints all possible different combinations of two digits.

Numbers must be separated by ,, followed by a space
The two digits must be different
01 and 10 are considered the same combination of the two digits 0 and 1
Print only the smallest combination of two digits
Numbers should be printed in ascending order, with two digits
The last number should be followed by a new line
You can only use no more than 3 print functions with string format
You can only use no more than 2 loops in your code
You are not allowed to store numbers or strings in a variable
You are not allowed to import any module
    
    for i in range(99):
We use two nested loops. The outer loop iterates through the first digit (num1) from 0 to 9.
The inner loop iterates through the second digit (num2) from num1 + 1 to 9. This ensures that
 we only get different digits and avoid repetitions.
Inside the loops, we check if the first digit (num1) is less than 8. If it is, we print the 
combination of digits followed by ", " using print("{:d}{:d}, ".format(num1, num2), end="").
If the first digit is 8, we print the combination of digits without 
the trailing ", " using print("{:d}{:d}".format(num1, num2)).
The {:d} inside the format() function ensures that the digits are 
printed as integers without leading zeros.
    
    
    """




