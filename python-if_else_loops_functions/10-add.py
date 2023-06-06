#!/usr/bin/python3
def add(a, b):
    return a + b

"""
          Write a function that adds two integers and returns the result.

Prototype: def add(a, b):
Returns the value of a + b
You are not allowed to import any module
You don’t need to understand __import__

guillaume@ubuntu:~/$ cat 10-main.py
#!/usr/bin/env python3
add = __import__('10-add').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))

guillaume@ubuntu:~/$ ./10-main.py
3
98
98
guillaume@ubuntu:~/$ 


"""

"""
        The function simply returns the sum of the two input integers a and b.
The + operator is used to perform the addition operation.
The result is returned from the function.

"""