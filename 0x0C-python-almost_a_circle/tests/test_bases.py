#!/usr/bin/python3
"""Unittest for Rectangle class

Variety of tests

"""
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """TestRectangle class

    Contains unittests for rectangle class

    """

    def setUp(self):
        """Set up test cases

        """
        self.rect = Rectangle(5, 10)
        self.x = self.rect.x
        self.w = self.rect.width
        self.h = self.rect.height
        self.id = self.rect.id
        self.y = self.rect.y
        self.print = (f"[Rectangle] ({self.id}) {self.x}/"
                      f"{self.y} - {self.w}/{self.h}")
        self.disp = "#####\n" * 10
        self.sq = Square(5)
        self.sqx = self.sq.x
        self.sqsize = self.sq.size
        self.sqid = self.sq.id
        self.sqy = self.sq.y
        self.sqprint = (f"[Square] ({self.sqid}) {self.sqx}/"
                        f"{self.sqy} - {self.sqsize}")
        self.sqdisp = "#####\n" * 5

    def test_one_argument(self):
        """Test out using large numbers

        """
        pass

    def test_str(self):
        """Test the __str__ method

        """
        self.assertEqual(str(self.rect), self.print)

    def test_area(self):
        """Test the area calculation

        """
        print("Area testing")
        self.assertEqual(self.rect.area(), 50)

    def test_display(self):
        """Test the area calculation

        """
        print("Display Rectangle testing")
        pass

    def test_update_id(self):
        """Test the update method

        """
        print("Update Rectangle.id testing")
        self.rect.update(54)
        self.assertEqual(self.rect.id, 54)

    def test_update_width(self):
        """Test the update method

        """
        print("Update Rectangle.width testing")
        self.rect.update(54, 45)
        self.assertEqual(self.rect.width, 45)

    def test_update_height(self):
        """Test the update method

        """
        print("Update Rectangle.height testing")
        self.rect.update(54, 45, 32)
        self.assertEqual(self.rect.height, 32)

    def test_update_x(self):
        """Test the update method

        """
        print("Update Rectangle.x testing")
        self.rect.update(54, 45, 32, 37)
        self.assertEqual(self.rect.x, 37)

    def test_update_y(self):
        """Test the update method

        """
        print("Update Rectangle.y testing")
        self.rect.update(54, 45, 32, 27, 67)
        self.assertEqual(self.rect.y, 67)

    def test_update_id_kwarg(self):
        """Test the update method

        """
        print("Update_kwarg Rectangle.id testing")
        self.rect.update(id=22)
        self.assertEqual(self.rect.id, 22)

    def test_update_width_kwarg(self):
        """Test the update method

        """
        print("Update_kwarg Rectangle.width testing")
        self.rect.update(width=90)
        self.assertEqual(self.rect.width, 90)

    def test_update_height_kwarg(self):
        """Test the update method

        """
        print("Update_kwarg Rectangle.height testing")
        self.rect.update(height=77)
        self.assertEqual(self.rect.height, 77)

    def test_update_x_kwarg(self):
        """Test the update method

        """
        print("Update_kwarg Rectangle.x testing")
        self.rect.update(x=80)
        self.assertEqual(self.rect.x, 80)

    def test_update_y_kwarg(self):
        """Test the update method

        """
        print("Update_kwarg Rectangle.y testing")
        self.rect.update(y=35)
        self.assertEqual(self.rect.y, 35)

    def test_args_width_string(self):
        print("Width testing")
        with self.assertRaises(TypeError):
            Rectangle("", 3)

    def test_args_width_negative(self):
        print("Width testing")
        with self.assertRaises(ValueError):
            Rectangle(-2, 3)

    def test_args_width_none(self):
        print("Width testing")
        with self.assertRaises(TypeError):
            Rectangle(None, 3)

    def test_args_width_zero(self):
        print("Width testing")
        with self.assertRaises(ValueError):
            Rectangle(0, 3)

    def test_args_height_string(self):
        print("Height testing")
        with self.assertRaises(TypeError):
            Rectangle(1, "")

    def test_args_height_negative(self):
        print("Height testing")
        with self.assertRaises(ValueError):
            Rectangle(1, -4)

    def test_args_height_none(self):
        print("Height testing")
        with self.assertRaises(TypeError):
            Rectangle(1, None)

    def test_args_height_zero(self):
        print("Height testing")
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_args_x_string(self):
        print("x testing")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "")

    def test_args_x_negative(self):
        print("x testing")
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -67)

    def test_args_x_none(self):
        print("x testing")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, None)

    def test_args_y_string(self):
        print("y testing")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "")

    def test_args_y_negative(self):
        print("y testing")
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -6)

    def test_args_y_none(self):
        print("y testing")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, None)

    def test_sq_str(self):
        """Test the __str__ method

        """
        self.assertEqual(str(self.sq), self.sqprint)

    def test_sq_area(self):
        """Test the area calculation

        """
        print("Area Square testing")
        self.assertEqual(self.sq.area(), 25)

    def test_sq_display(self):
        """Test the area calculation

        """
        print("Display Square testing")
        pass

    def test_update_sq_id(self):
        """Test the update method

        """
        print("Update Square.id testing")
        self.sq.update(54)
        self.assertEqual(self.sq.id, 54)

    def test_update_sq_size(self):
        """Test the update method

        """
        print("Update Square.size testing")
        self.sq.update(54, 45)
        self.assertEqual(self.sq.size, 45)

    def test_update_sq_x(self):
        """Test the update method

        """
        print("Update Square.x testing")
        self.sq.update(54, 45, 27)
        self.assertEqual(self.sq.x, 27)

    def test_update_sq_y(self):
        """Test the update method

        """
        print("Update Square.y testing")
        self.sq.update(54, 45, 27, 78)
        self.assertEqual(self.sq.y, 78)


if __name__ == '__main__':
    unittest.main()
