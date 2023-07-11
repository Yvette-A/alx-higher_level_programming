#!/usr/bin/python3
"""Defines a module appernd_write"""


def append_write(filename="", text=""):
    """
    It appends a string at the end of a text
    file and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        return (a_file.write(text))
