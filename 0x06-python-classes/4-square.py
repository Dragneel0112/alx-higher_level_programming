#!/usr/bin/python3
""" Defines class Square """


class Square:
    """ Represents Square """
    def __init__(self, size=0):
        """ Initialize Square.
        Args:
            size (int): size of Square """
        self.size = size

    @property
    def size(self):
        """ Getter and setter for size of Square """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return area of the Square """
        return (self.__size * self.__size)
