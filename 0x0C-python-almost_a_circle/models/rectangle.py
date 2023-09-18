#!/usr/bin/python3
"""My rectangle module

Contains Rectangle class

"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class

    Contains Rectangle plus attributes

    Methods:
    __init__(self, width, height, x=0, y=0, id=None):

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id)
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width == 0 or width < 0:
            raise ValueError('width must be > 0')
        self.__width = width
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height == 0 or height < 0:
            raise ValueError('height must be > 0')
        self.__height = height
        if type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x
        if type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    @property
    def width(self):
        """width getter
        Gets width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value == 0 or value < 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Height getter
        Gets height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value == 0 or value < 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value
            print(self.__height)

    @property
    def x(self):
        """x getter
        Gets x
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """y getter
        Gets y
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """Area of rectangle
        Calculates rectangle area
        """
        return self.__width * self.__height

    def display(self):
        """Dispay method
        Displays rectangle as #
        """
        for _ in range(self.__y):
            print("")
        for item in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """String method
        String representation of class
        """
        return (f"[Rectangle] ({self.id}) {self.__x}/"
                f"{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Update method
        Assigns an argument to each method
        """
        if args and len(args) != 0:
            for i, item in enumerate(args):
                if i == 0:
                    self.id = item
                elif i == 1:
                    self.__width = item
                elif i == 2:
                    self.__height = item
                elif i == 3:
                    self.__x = item
                elif i == 4:
                    self.__y = item
        elif kwargs:
            self.id = kwargs.get('id', self.id)
            self.__width = kwargs.get('width', self.__width)
            self.__height = kwargs.get('height', self.__height)
            self.__x = kwargs.get('x', self.__x)
            self.__y = kwargs.get('y', self.__y)

    def to_dictionary(self):
        """To_dictionary method
        Return dictionary representation of class
        """
        my_dict = vars(self)
        returned = dict()
        for key, value in my_dict.items():
            if "width" in key:
                returned["width"] = value
            elif "height" in key:
                returned["height"] = value
            elif "id" in key:
                returned["id"] = value
            elif "x" in key:
                returned["x"] = value
            elif "y" in key:
                returned["y"] = value
        return returned
