#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def setUp(self):
        self.list1 = [1, 2, 3, 4, 5]
        self.list2 = [-2, -10, -30]

    def test_positive(self):
        self.assertEqual(max_integer(self.list1), 5)

    def test_negative(self):
        self.assertEqual(max_integer(self.list2), -2)

    def test_empty(self):
        self.assertEqual(max_integer(), None)


if __name__ == "__main__":
    unittest.main()
