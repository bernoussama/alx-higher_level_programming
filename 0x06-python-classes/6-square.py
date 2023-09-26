#!/usr/bin/python3
"""
Square Module
"""


class Square:
    """
    Square Class
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = self.size(size)
        self.__position = self.position(position)

    def area(self):
        """
        Returns area of the square
        """
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        if self.size > 0:
            if self.position[1] > 0:
                print(*["#" * self.size for _ in range(self.size)], sep="\n")
            else:
                print(
                    *[
                        (" " * self.position[0]) + ("#" * self.size)
                        for _ in range(self.size)
                    ],
                    sep="\n"
                )

        else:
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            if all(isinstance(el, int) and el > 0 for el in value):
                self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
