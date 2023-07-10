#!/usr/bin/python3

"""definges a module that checks if isinstance"""


def is_same_class(obj, a_class):
    """returns if the object is an instance of a class or not"""
    if type(obj) == a_class:
        return True
    return False
