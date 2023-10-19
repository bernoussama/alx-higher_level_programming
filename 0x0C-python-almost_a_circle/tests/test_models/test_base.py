import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_initialization(self):
        """
        Test the initialization of a Base instance.
        """
        base_instance = Base()
        self.assertIsInstance(base_instance, Base)

    def test_id_auto_increment(self):
        """
        Test if the id attribute auto-increments correctly.
        """
        base_instance1 = Base()
        base_instance2 = Base()
        self.assertEqual(base_instance2.id, base_instance1.id + 1)

    def test_custom_id(self):
        """
        Test if a custom ID is correctly assigned.
        """
        custom_id = 42
        base_instance = Base(custom_id)
        self.assertEqual(base_instance.id, custom_id)

    def test_to_json_string(self):
        """
        Test the to_json_string method.
        """
        data = [{"key1": "value1", "key2": "value2"}]
        json_string = Base.to_json_string(data)
        self.assertEqual(json_string, '[{"key1": "value1", "key2": "value2"}]')

    def test_save_to_file(self):
        """
        Test the save_to_file method.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                file.read(),
                '[{"id": 10, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 11, "width": 2, "height": 4, "x": 0, "y": 0}]',
            )

    def test_from_json_string(self):
        """
        Test the from_json_string method.
        """
        json_string = '[{"key1": "value1", "key2": "value2"}]'
        data = Base.from_json_string(json_string)
        self.assertEqual(data, [{"key1": "value1", "key2": "value2"}])

    def test_create(self):
        """
        Test the create method.
        """
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        rectangle_instance = Rectangle.create(**r1_dict)
        self.assertEqual(rectangle_instance.x, 1)
        self.assertEqual(rectangle_instance.width, 3)
        self.assertEqual(rectangle_instance.height, 5)

    def test_load_from_file(self):
        """
        Test the load_from_file method.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        loaded_data = Rectangle.load_from_file()
        self.assertEqual(len(loaded_data), 2)
        self.assertEqual(loaded_data[0].width, 10)
        self.assertEqual(loaded_data[1].height, 4)


if __name__ == "__main__":
    unittest.main()
