#!/usr/bin/python3
"""
Square module

"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """__str__ method for Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Updates Rectangle instance"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for (
                i,
                arg,
            ) in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)
