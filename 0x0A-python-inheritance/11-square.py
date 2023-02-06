#!/usr/bin/python3
"""
Class Square that inherits from Rectangle
add calculate area and size
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """calculate size and validate with integer validator"""
    def __init__(self, size):
        """checks for int and return area"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
        """super used to modify parent class"""

    def __str__(self):
        """print rectangle width/height"""
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
