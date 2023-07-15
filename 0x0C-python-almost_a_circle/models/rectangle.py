#!/usr/bin/python3
"""defines a rectangle"""
from .base import Base


class Rectangle(Base):
    """represents a cass rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """defines the properties of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the properties of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self, value):
        """defines the propeties of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the property of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def y(self):
        """defines the properties of the y cordinates"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the properties of the y cordinates"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """defines the properties of the x cordinates"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """ return the area of a rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """prints the class rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print()

    def __str__(self):
        """prints the string representation of a rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)
