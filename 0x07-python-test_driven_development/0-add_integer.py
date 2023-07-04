#!/usr/bin/python3

"""
an addition function.
a is the first value given
b is the second value and it is iptional.
"""


def add_integer(a, b=98):
    """
    adds two numbers and returns and integer.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
