#!/usr/bin/python3
"""class rectangle defines a rectangle"""


class Rectangle:
    """defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return the area of a rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))

    def __str__(self):
        """ Prints a string character of representation of class rectacngle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = []
        for i in range(self.__height):
            [rectangle.append(str(self.print_symbol))for
             j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __del__(self):
        """Print a message when a rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
