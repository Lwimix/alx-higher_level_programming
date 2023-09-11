#!/usr/bin/python3
"""My BaseGeometry module

Contains an BaseGeometry class and Rectangle class

"""


class BaseGeometry:
    """My BaseGeometry class
    It contains area method

    Methods:
    area(self):
    integer_validator(self, name, value):
    """
    def area(self):
        """My area method
        It raises an exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Integer validator method
        Verifies value is a positive integer
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """My Rectangle class
    Inherits from BaseGeometry

    Methods:
    __init__(self, width, height):
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def integer_validator(self, name, value):
        """Integer validator method
        Verifies value is a positive integer
        """
        return super().integer_validator(name, value)
