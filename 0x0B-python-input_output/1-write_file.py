#!/usr/bin/python3
"""defines a module write_file"""


def write_file(filename="", text=""):
    """
    writes a string to a txt file and returns
    the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        return (a_file.write(text))
