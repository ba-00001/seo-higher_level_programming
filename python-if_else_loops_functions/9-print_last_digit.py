#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False



"""
           7. islower
        mandatory
        Write a function that checks for lowercase character.
        
        Prototype: def islower(c):
        Returns True if c is lowercase
        Returns False otherwise
        You are not allowed to import any module
        You are not allowed to use str.upper() and str.isupper()
        Tips: ord()
        You don’t need to understand __import__


"""

"""
        The ord() function is used to get the ASCII value of the character c.
        Lowercase letters in ASCII range from 97 to 122.
        We compare the ASCII value of c with this range to check if it is lowercase.
        If the condition is satisfied, we return True; otherwise, we return False.

"""