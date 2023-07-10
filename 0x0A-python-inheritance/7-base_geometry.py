#!/usr/bin/python3

""" defines a class"""


class BaseGeometry():
    """a class of BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
