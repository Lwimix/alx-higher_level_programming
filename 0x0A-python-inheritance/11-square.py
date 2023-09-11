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
    rect = "[Rectangle] "

    def __init__(self, width, height):
        super().integer_validator("", width)
        self.__width = width
        super().integer_validator("", height)
        self.__height = height

    def integer_validator(self, name, value):
        """Integer validator method
        Verifies value is a positive integer
        """
        return super().integer_validator(name, value)

    def area(self):
        """Area method
        Calculates area of Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Str method
        Prints class as a string
        """
        return self.rect + str(self.__width) + "/" + str(self.__height)


class Square(Rectangle):
    """My Square class
    Inherits from Rectangle

    Methods:
    __init__(self, size):
    """
    def __init__(self, size):
        super().integer_validator("", size)
        self.__size = size
        self.rect = "[Square] "

        Rectangle.__init__(self, size, size)
