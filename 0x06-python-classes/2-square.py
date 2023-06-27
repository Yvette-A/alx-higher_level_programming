#!/usr/bin/python3
"""defines a class square"""


class Square:
    """defines a class square and instantiates it
    wit a private attribute size.
    """
    def __init__(self, size):
        """instantiates a square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
