#!/usr/bin/python3
""" My class module
"""


class MyClass:
    """ My class
    """

    s = 0

    def __init__(self, n, num=4):
        self.__n = n
        self.num = num
        self.is_team_red = (self.num % 2) == 0

    def win(self):
        self.s += 1

    def lose(self):
        self.s -= 1

    def __str__(self):
        return "[MyClass] {} - {:d} => {:d}".format(self.__n, self.num, self.s)
