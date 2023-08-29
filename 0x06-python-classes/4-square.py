#!/usr/bin/python3
"""The Beginning of a square's creation
"""


class Square:
    """A Square shape

    Creates a square shape with various properties

    Methods:
        __init__(self, size=0): intializes class attributes
    """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """Determines the area of our square
        Returns:
            the area of the square, an error otherwise
        """
        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')
        else:
            return self.__size ** 2

    @property
    def size(self):
        """The size given as our square size"""
        return self.__size

    @size.setter
    def size(self, value):
        try:
            if not isinstance(value, int):
                raise TypeError('size must be an integer')
            elif value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        except ValueError as e:
            print(f"{e}")
