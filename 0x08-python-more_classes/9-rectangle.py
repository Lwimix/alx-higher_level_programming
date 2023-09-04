#!/usr/bin/python3
"""My Rectangle Class



"""


class Rectangle:
    """Class rectangle
    Creates a rectangle shape with various properties

    Methods:
        __init__(self, width=0, height=0): intializes class attributes
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        self.__class__.number_of_instances += 1

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

    def __str__(self):
        """Returns a string of our rectangle in the form of hashes

        """
        if self.__width == 0 or self.__height == 0:
            return ""
        my_str = ""
        for item in range(self.__height):
            my_str += str(self.print_symbol) * self.__width
            if item < self.__height - 1:
                my_str += "\n"
        return my_str

    def __repr__(self):
        """Returns a true string of our rectangle

        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Deletes an instance of our rectangle after use

        """
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method used for comparing two rectangles' areas

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new class which is a square

        """
        return cls(size, size)
