#!/usr/bin/python3
"""The Square module

Contains the Square class

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class

    Contains attributes of a square

    Inherits from Rectangle class

    Methods:
    __init__(self, size, x=0, y=0, id=None):
    """

    def __init__(self, size, x=0, y=0, id=None):
        self.__size = size
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """String Method
        String representation of Square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__size}"

    @property
    def size(self):
        """Size getter
        Gets size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__size = value
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """Update method
        Assigns an argument to each method
        """
        if args and len(args) != 0:
            for i, item in enumerate(args):
                if i == 0:
                    self.id = item
                elif i == 1:
                    self.__size = item
                elif i == 2:
                    self.x = item
                elif i == 3:
                    self.y = item
        elif kwargs:
            self.id = kwargs.get('id', self.id)
            self.__size = kwargs.get('size', self.__size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """to_dicionary method
        Returns dictionary representation of class
        """
        my_dict = vars(self)
        returned = dict()
        my_keys = ["id", "x", "y", "size"]
        for key, value in my_dict.items():
            for item in my_keys:
                if item in key:
                    returned[item] = my_dict[key]
        return returned
