#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        self.Base = Base

    def tearDown(self):
        print("tearing down...")

    def test_autoIncrement(self):
        base = self.Base()
        b2 = self.Base()
        b3 = self.Base()

        id = base.id
        expected = 1
        self.assertEqual(id, expected, f"wrong id expecting {expected}, got {id}")

        id = b2.id
        expected = 2
        self.assertEqual(id, expected, f"wrong id expecting {expected}, got {id}")

        id = b3.id
        expected = 3
        self.assertEqual(id, expected, f"wrong id expecting {expected}, got {id}")

    def test_customID(self):
        b4 = self.Base(12)

        id = b4.id
        expected = 12
        self.assertEqual(id, expected, f"wrong id expecting {expected}, got {id}")

    def test_autoIncrementAfterCustom(self):
        b5 = self.Base()

        id = b5.id
        expected = 4
        self.assertEqual(id, expected, f"wrong id expecting {expected}, got {id}")


if __name__ == "__main__":
    unittest.main()
