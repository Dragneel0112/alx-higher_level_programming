#!/usr/bin/python3
"""
Class Rectangle that inherits from BaseGeometry
add width and heigth
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """create subclass Rectangle of BaseGeometry"""
    def __init__(self, width, height):
        """
        width and height private
        and must be positive integer
        """
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
