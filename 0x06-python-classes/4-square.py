#!/usr/bin/python3
"""defines a class square"""


class Square:
    """defines a class square and instantiates it
    wit a private attribute size.
    """
    def __init__(self, size):
        """instantiates a square"""
        self.size = size

    def size(self, value):
        """setter for the size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def size(self):
        """retrieves the size of the square."""
        return (self.__size)

    def area(self):
        """Return the current square area."""
        return (self.__size * self.__size)
