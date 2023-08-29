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

    @property
    def size(self):
        """The size given as our square size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(type(self.__size), int):
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
