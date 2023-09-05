#!/usr/bin/python3
"""My add integer module
Has one function that adds two integers
a and b are the integers used in addition
the result of their addition is returned
"""


def add_integer(a, b=98):
    """Adds two integers together returning their result
    Both a and b should be integers so as to be added
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    a, b = int(a), int(b)
    return a + b
