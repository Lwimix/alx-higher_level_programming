#!/usr/bin/python3
class Square:
    """
    Creates a square

    Methods:
        __init__(self, size=0): intializes class attributes
    """
    def __init__(self, size=0, position=(0, 0)):
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
        if not isinstance(type(size), int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        integers = all(isinstance(i, int) for i in self.__position)
        if len(self.__position) < 2 or not integers:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            printed = "#"
            for i in range(self.__size):
                for x in range(self.__size):
                    print("{}".format(printed), end="")
                print("")
