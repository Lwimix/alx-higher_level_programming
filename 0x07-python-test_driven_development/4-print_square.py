#!/usr/bin/python3
"""My print_square module
Contains print_square() which prints a square of hashes
No importing done, no unique functions
Prints the final square of hashes
"""


def print_square(size):
    """Prints a square of hashes
    Takes in a size for the square of type int
    """
    if (isinstance(size, float) and size < 0) or not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for item in range(size):
        for item in range(size):
            print("#", end="")
        print("")
