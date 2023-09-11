#!/usr/bin/python3
"""My MyList module

Contains the class, MyList

"""


class MyList(list):
    def print_sorted(self):
        """Print_sorted method
        Prints a sorted list
        """
        sorting = self[:]
        sorting.sort()
        print(sorting)
