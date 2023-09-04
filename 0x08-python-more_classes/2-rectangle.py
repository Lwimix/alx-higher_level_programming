#!/usr/bin/python3
"""My Rectangle Class



"""


class Rectangle:
    """Class rectangle
    Creates a rectangle shape with various properties

    Methods:
        __init__(self, width=0, height=0): intializes class attributes
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This is the width of our rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """This is the height of our rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculates the area of our rectangle

        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of our rectangle

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
