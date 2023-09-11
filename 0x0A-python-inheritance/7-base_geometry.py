#!/usr/bin/python3
"""My BaseGeometry module

Contains an empty geometry module

"""


class BaseGeometry:
    """My BaseGeometry class
    It contains area method
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
