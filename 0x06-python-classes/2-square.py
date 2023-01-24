#!/usr/bin/python3
""" Defines class Square """


class Square:
    """ Represents Square """
    def __init__(self, size=0):
        """ Initialize Square.
        Args:
            size (int): The size of Square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
