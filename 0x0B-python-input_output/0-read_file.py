#!/usr/bin/python3
"""defines a function read_file"""


def read_file(filename=""):
    """reads text file decoded in UTF8 and prints it is stdout"""
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")
