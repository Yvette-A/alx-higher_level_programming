#!/usr/bin/python3

"""defines a function that checkes the subclass"""


def inherits_from(obj, a_class):
    """ checkes whether is subclass or not"""
    return (issubclass(type(obj), a_class))
