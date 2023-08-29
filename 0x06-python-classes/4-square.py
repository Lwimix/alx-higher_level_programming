#!/usr/bin/python3
class Square:
    """
    Creates a square

    Methods:
        __init__(self, size=0): intializes class attributes
    """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        if not isinstance(type(self.__size), int):
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')
        else:
            return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(type(self.__size), int):
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
