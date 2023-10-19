#!/usr/bin/python3
"""Unittests for base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unitest for testing Base class"""

    def test_autoIncrement(self):
        base = Base()
        b2 = Base()

        id = b2.id
        expected = base.id + 1
        self.assertEqual(id, expected, f"wrong id expecting {expected}, got {id}")

    def test_customID(self):
        b4 = Base(12)

        id = b4.id
        expected = 12
        self.assertEqual(id, expected, f"wrong id expecting {expected}, got {id}")

    def test_autoIncrementAfterCustom(self):
        b5 = Base()

        id = b5.id
        expected = 3
        self.assertEqual(id, expected, f"wrong id expecting {expected}, got {id}")


if __name__ == "__main__":
    unittest.main()
