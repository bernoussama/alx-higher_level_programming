import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def test_square_creation(self):
        """
        Test the creation of a Square instance.
        """
        square_instance = Square(5)
        self.assertIsInstance(square_instance, Square)
        self.assertEqual(square_instance.size, 5)
        self.assertEqual(square_instance.x, 0)
        self.assertEqual(square_instance.y, 0)
        self.assertEqual(square_instance.id, 40)

    def test_size_property(self):
        """
        Test the size property.
        """
        square_instance = Square(3)
        square_instance.size = 6
        self.assertEqual(square_instance.size, 6)
        self.assertEqual(square_instance.width, 6)
        self.assertEqual(square_instance.height, 6)

    def test_str_method(self):
        """
        Test the __str__ method.
        """
        square_instance = Square(4, 1, 2, 99)
        string_representation = str(square_instance)
        self.assertEqual(string_representation, "[Square] (99) 1/2 - 4")

    def test_update_method_args(self):
        """
        Test the update method with *args.
        """
        square_instance = Square(2)
        square_instance.update(1, 3, 4, 5)
        self.assertEqual(square_instance.id, 1)
        self.assertEqual(square_instance.size, 3)
        self.assertEqual(square_instance.x, 4)
        self.assertEqual(square_instance.y, 5)

    def test_update_method_kwargs(self):
        """
        Test the update method with **kwargs.
        """
        square_instance = Square(2)
        square_instance.update(id=1, size=3, x=4, y=5)
        self.assertEqual(square_instance.id, 1)
        self.assertEqual(square_instance.size, 3)
        self.assertEqual(square_instance.x, 4)
        self.assertEqual(square_instance.y, 5)

    def test_to_dictionary_method(self):
        """
        Test the to_dictionary method.
        """
        square_instance = Square(3, 2, 1, 42)
        dictionary = square_instance.to_dictionary()
        expected_dict = {
            "id": 42,
            "size": 3,
            "x": 2,
            "y": 1,
        }
        self.assertEqual(dictionary, expected_dict)


if __name__ == "__main__":
    unittest.main()
