#!/usr/bin/python3
"""My MyList module

Contains the class, MyList

"""
class MyList(list):
    def print_sorted(self):
        """Print_sorted method
        Prints a sorted list
        """
        sorting = self
        smallest = sorting[0]
        ind = 0
        my_sort = []
        i = 0
        for item in sorting:
            while (i < len(sorting)):
                if sorting[i] <= smallest:
                    smallest = sorting[i]
                i = i + 1
            my_sort.append(smallest)
            ind = ind + 1
            if ind < len(sorting):
                smallest = sorting[ind]
            i = ind
        return my_sort
