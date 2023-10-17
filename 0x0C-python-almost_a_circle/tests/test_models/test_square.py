#!/usr/bin/python3

import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self) -> None:
        self.Square = Square

    def testIds(self):
        r1 = self.Square(10)
        r2 = self.Square(2)
        r3 = self.Square(2, 0, 1, 12)
        id = r1.id
        self.assertEqual(id, 1)
        id = r2.id
        self.assertEqual(id, 2)
        id = r3.id
        self.assertEqual(id, 12)

    def test_init_values(self):
        with self.assertRaises(ValueError):
            r = Square(0)
        with self.assertRaises(ValueError):
            r = Square(20, -4)
        with self.assertRaises(ValueError):
            r = Square(20, 2, -3)

    def test_area(self):
        r1 = Square(3)
        self.assertEqual(r1.area(), 3**2)
        r3 = Square(8, 0, 0, 12)
        self.assertEqual(r3.area(), 8**2)

    def test_update(self):
        r1 = Square(10, 10, 10, 10)

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
