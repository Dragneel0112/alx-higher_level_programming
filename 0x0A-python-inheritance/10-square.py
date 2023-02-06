#!/usr/bin/python3
"""
Class Square that inherits from Rectangle (9-rectangle.py)
add calculate area and size
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """calculate size and check if int"""
    def __init__(self, size):
        """checks for int and return area"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
        """super used to modify parent class"""
