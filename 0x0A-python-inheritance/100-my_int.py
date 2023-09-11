#!/usr/bin/python3
"""My MyInt module

Contains MyInt class

"""


class MyInt():
    """MyInt class
    Overrides != and ==

    Methods:
    __init__(self, value)
    """
    def __init__(self, value):
        self.value = value

    def __ne__(self, other):
        """Ne method
        Inverts use of !=
        """
        return self.value == other

    def __eq__(self, other):
        """Eq method
        Inverts use of ==
        """
        return self.value != other

    def __str__(self):
        return str(self.value)
