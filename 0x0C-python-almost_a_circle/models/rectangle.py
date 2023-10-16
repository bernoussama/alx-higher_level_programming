#!/usr/bin/python3
"""
Rectangle module

"""

from models.base import Base


class Rectangle(Base):
    """Rectange class

    extending Base class

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init func"""

        super().__init__(id)

        name = "width"
        value = width
        self.validate_int(value, name)
        self.validate_length(value, name)
        self.__width = width

        name = "height"
        value = height
        self.validate_int(value, name)
        self.validate_length(value, name)
        self.__height = height

        name = "x"
        value = x
        self.validate_int(value, name)
        self.validate_position(value, name)
        self.__x = x

        name = "y"
        value = y
        self.validate_int(value, name)
        self.validate_position(value, name)
        self.__y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """width setter"""

        name = "width"
        self.validate_int(value, name)
        self.validate_length(value, name)
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        name = "height"
        self.validate_int(value, name)
        self.validate_length(value, name)
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter"""
        name = "x"
        self.validate_int(value, name)
        self.validate_position(value, name)
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        name = "y"
        self.validate_int(value, name)
        self.validate_position(value, name)
        self.__y = value

    def area(self):
        """area method
        returns the rectangle area
        """
        return self.width * self.height

    def display(self):
        """display method
        prints in stdout the Rectangle instance with the character #
        """
        row = "#" * self.width
        rec = "\n".join([row for _ in range(self.height)])
        print(rec)

    def __str__(self):
        return (
            f"[Rectangle] ({ self.id }) { self.x }/{ self.y }"
            + f" - { self.width }/{ self.height }"
        )

    def validate_int(self, value, name):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

    def validate_length(self, value, name):
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def validate_position(self, value, name):
        if value < 0:
            raise ValueError(f"{name} must be >= 0")
