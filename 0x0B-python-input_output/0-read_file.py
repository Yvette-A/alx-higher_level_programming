#!/usr/bin/python3
"""defines a module read_file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as a_file:
        data = a_file.read()
        print(data, end="")
