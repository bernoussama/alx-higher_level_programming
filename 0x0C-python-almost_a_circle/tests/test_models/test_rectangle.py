#!/usr/bin/python3
""" Rectangle unittests"""

import unittest
from unittest.mock import patch
from io import StringIO
import json

from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.Rectangle = Rectangle

    def testIds(self):
        r1 = self.Rectangle(10, 2)
        r2 = self.Rectangle(2, 10)
        r3 = self.Rectangle(2, 10, 0, 1, 12)
        id = r1.id
        self.assertEqual(id, 12)
        id = r2.id
        self.assertEqual(id, 13)
        id = r3.id
        self.assertEqual(id, 12)

    def test_validate_int(self):
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.validate_int("2", "width")
        with self.assertRaises(TypeError):
            r.validate_int([], "width")
        with self.assertRaises(TypeError):
            r.validate_int({}, "width")
        with self.assertRaises(TypeError):
            r.validate_int(2.0, "width")

    def test_validate_length(self):
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.validate_length(0, "width")
        with self.assertRaises(ValueError):
            r.validate_length(-10, "width")

    def test_validate_position(self):
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.validate_position(-1, "width")
        with self.assertRaises(ValueError):
            r.validate_position(-10, "width")

    def test_width_type(self):
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.width = "10"
        with self.assertRaises(TypeError):
            r.width = 2.0
        with self.assertRaises(TypeError):
            r.width = [1]
        with self.assertRaises(TypeError):
            r.width = {"w": 1}

    def test_height_type(self):
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.height = "10"
        with self.assertRaises(TypeError):
            r.height = 2.0
        with self.assertRaises(TypeError):
            r.height = [1]
        with self.assertRaises(TypeError):
            r.height = {"h": 1}

    def test_x_type(self):
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.x = "10"
        with self.assertRaises(TypeError):
            r.x = 2.0
        with self.assertRaises(TypeError):
            r.x = [1]
        with self.assertRaises(TypeError):
            r.x = {"w": 1}

    def test_y_type(self):
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.y = "10"
        with self.assertRaises(TypeError):
            r.y = 2.0
        with self.assertRaises(TypeError):
            r.y = [1]
        with self.assertRaises(TypeError):
            r.y = {"w": 1}

    def test_width_value(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(ValueError):
            r.width = 0

    def test_height_value(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.height = -10
        with self.assertRaises(ValueError):
            r.height = 0

    def test_x_value(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.x = -10
        with self.assertRaises(ValueError):
            r.x = -1

    def test_y_value(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.y = -10
        with self.assertRaises(ValueError):
            r.y = -1

    def test_init_types(self):
        with self.assertRaises(TypeError):
            r = Rectangle("10", 20)
        with self.assertRaises(TypeError):
            r = Rectangle(20, "10")
        with self.assertRaises(TypeError):
            r = Rectangle(20, 10, "10")
        with self.assertRaises(TypeError):
            r = Rectangle(20, 10, 2, "10")

    def test_init_values(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 20)
        with self.assertRaises(ValueError):
            r = Rectangle(20, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(20, 10, -4)
        with self.assertRaises(ValueError):
            r = Rectangle(20, 10, 2, -3)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 3 * 2)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 8 * 7)

    def test_display(self):
        r = Rectangle(2, 2)
        rec2_2 = "##\n##"
        rec4_6 = "####\n####\n####\n####\n####\n####"
        rec_pos = """

  ##
  ##
  ##
"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            r.display()
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, rec2_2)

        r = Rectangle(4, 6)
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            r.display()
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, rec4_6)
        r = Rectangle(2, 3, 2, 2)
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            r.display()
            output = mock_stdout.getvalue()
            self.assertEqual(output, rec_pos)

    def test_str(self):
        r = Rectangle(2, 2, 2, 2, 12)
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            print(r)
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "[Rectangle] (12) 2/2 - 2/2")

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)

        r1.update(89, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

        r1.update(height=1)
        self.assertEqual(r1.height, 1)

        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 1)

    def test_to_json_string(self):
        r1 = Rectangle(10, 10, 10, 10)
        dict = r1.to_dictionary()
        self.assertEqual(Base.to_json_string(dict), json.dumps(dict))


if __name__ == "__main__":
    unittest.main()
