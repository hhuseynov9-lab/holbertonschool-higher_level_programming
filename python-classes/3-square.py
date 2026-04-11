#!/usr/bin/python3
"""
Square class-ı üçün modul.
"""


class Square:
    """
    Kvadratı təmsil edən sinif.
    """

    def __init__(self, size=0):
        """
        Kvadratı yaradır.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Sahəni hesablayır.
        """
        return self.__size * self.__size
