#!/usr/bin/python3
"""function that adds 2 integers"""


def add_integer(a, b=98):
    """this function returns the add of two numbers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
