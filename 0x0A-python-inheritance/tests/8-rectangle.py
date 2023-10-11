``base_geometry`` module

--------------------------
--------------------------

``base_geometry`` class

    >>> BaseGeometry = __import__('7-base_geometry').BaseGeometry

    >>> bg = BaseGeometry()

    >>> bg.integer_validator("my_int", 12)

    >>> bg.area()
    Traceback (most recent call last):
        ...
    Exception: area() is not implemented

    >>> bg.integer_validator("name", "John")
    Traceback (most recent call last):
        ...
    TypeError: name must be an integer

    >>> bg.integer_validator("name",[1,])
    Traceback (most recent call last):
        ...
    TypeError: name must be an integer

    >>> bg.integer_validator("name",(1,))
    Traceback (most recent call last):
        ...
    TypeError: name must be an integer

    >>> bg.integer_validator("name",1.0)
    Traceback (most recent call last):
        ...
    TypeError: name must be an integer

    >>> bg.integer_validator("age", 0)
    Traceback (most recent call last):
        ...
    ValueError: age must be greater than 0

    >>> bg.integer_validator("age")
    Traceback (most recent call last):
        ...
    TypeError: BaseGeometry.integer_validator() missing 1 required positional argument: 'value'

