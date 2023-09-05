#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def large_numbers(self):
        """Tests out using large numbers

        """
        output = max_integer([222220000000, 3333333333399999, 20])
        self.AssertEqual(output, 3333333333399999)

    def regular_numbers(self):
        """Tests out using regular small numbers
        """
        output = max_integer([20, 33, 67, 134])
        self.AssertEqual(output, 134)

    def empty_list(self):
        """Tests out using an empty list

        """
        output = max_integer([])
        self.AssertEqual(output, None)

    def negative_numbers(self):
        """Tests out using negative numbers

        """
        output = max_integer([-34, 26, 67, -120, 45])
        self.AssertEqual(output, 67)

    def duplicate_numbers(self):
        """Tests out using duplicate numbers

        """
        output = max_integer([7, 7, 7, 7, 7, 7])
        self.AssertEqual(output, 7)

    def single_number(self):
        """Tests out using a single number

        """
        output = max_integer([4])
        self.AssertEqual(output, 4)


if __name__ == '__main__':
    unittest.main()
