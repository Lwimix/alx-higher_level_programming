#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_large_numbers(self):
        """Tests out using large numbers

        """
        output = max_integer([222220000000, 3333333333399999, 20])
        self.assertEqual(output, 3333333333399999)

    def test_regular_numbers(self):
        """Tests out using regular small numbers
        """
        output = max_integer([20, 33, 67, 134])
        self.assertEqual(output, 134)

    def test_empty_list(self):
        """Tests out using an empty list

        """
        output = max_integer([])
        self.assertEqual(output, None)

    def test_negative_numbers(self):
        """Tests out using negative numbers

        """
        output = max_integer([-34, -26, -67, -120, -45])
        self.assertEqual(output, -26)

    def test_duplicate_numbers(self):
        """Tests out using duplicate numbers

        """
        output = max_integer([7, 7, 7, 7, 7, 7])
        self.assertEqual(output, 7)

    def test_single_number(self):
        """Tests out using a single number

        """
        output = max_integer([4])
        self.assertEqual(output, 4)

    def test_max_in_beginning(self):
        """Tests out using a single number

        """
        output = max_integer([200, 78, 90])
        self.assertEqual(output, 200)

    def test_one_negative_number(self):
        """Tests out using a single number

        """
        output = max_integer([4, -900, 34, 65])
        self.assertEqual(output, 65)


if __name__ == '__main__':
    unittest.main()
