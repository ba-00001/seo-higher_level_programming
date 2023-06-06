#!/usr/bin/python3
def pow(a, b):
    return a ** b


"""
          11. a ^ b
mandatory
Write a function that computes a to the power of b and return the value.

Prototype: def pow(a, b):
Returns the value of a ^ b
You are not allowed to import any module
You don’t need to understand __import__

guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/env python3
pow = __import__('11-pow').pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))

guillaume@ubuntu:~/$ ./11-main.py
4
9604
1
0.0001
-1024
guillaume@ubuntu:~/$ 

"""

"""
 The function uses the ** operator to perform the exponentiation operation.
The first parameter a is the base, and the second parameter b is the exponent.
The result of a raised to the power of b is returned from the function.

"""