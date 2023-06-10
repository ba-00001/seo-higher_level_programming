#!/usr/bin/python3
for num in range(100):
    if num < 99:
        print("{:02d}, ".format(num), end="")
    else:
        print("{:02d}".format(num))


    """
    We use a loop to iterate through the numbers from 0 to 99 using the range(100) function.
Inside the loop, we check if the current number (num) is less than 99. If it is, we print 
the formatted number followed by ", " using print("{:02d}, ".format(num), end="").
If the current number is 99, we print it without the trailing ", " using print("{:02d}".format(num)).
The {:02d} inside the format() function ensures that the numbers are formatted with 
two digits, padded with leading zeros if necessary.

This code satisfies the requirements of printing the numbers separated 
by ", ", in ascending order, with two digits, and the last number followed 
by a new line. It uses a maximum of two print functions with string format and only one loop, as specified.
    
    """




