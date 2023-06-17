#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If a tuple is smaller than 2, use the value 0 for each missing integer
    # If a tuple is bigger than 2, use only the first 2 integers
    a = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    b = tuple_b[:2] + (0,) * (2 - len(tuple_b))

    # The first element of the resulting tuple is the addition of the first elements of each argument
    # The second element of the resulting tuple is the addition of the second elements of each argument
    result = (a[0] + b[0], a[1] + b[1])

    return result

