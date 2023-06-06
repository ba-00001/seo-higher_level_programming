#!/usr/bin/python3
for i in range(99):
    print(f"{i} = 0x{i:x}")

    """
    for i in range(99):

This sets up a loop that iterates over the numbers from 0 to 98 (99 is excluded) using the range() function.
print(f"{i} = 0x{i:x}")

This is the print statement that combines decimal and hexadecimal representations of the current number i.
The f-string notation is used with the print() function to format the output.
Inside the f-string, {i} represents the decimal representation of the current number, 
and {i:x} represents the hexadecimal representation of the current number.
The :x format specifier is used to format the number as a lowercase hexadecimal value.
The code will print each number from 0 to 98 along with its decimal and hexadecimal representations, as shown in the example output.
    
    
    """




