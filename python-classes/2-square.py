#!/usr/bin/python3
"""
Bu modul type() funksiyası ilə yoxlama aparan Square sinfini təyin edir.
"""


class Square:
    """
    Kvadratı təyin edən sinif.
    """

    def __init__(self, size=0):
        """
        Yeni bir Square yaradır.

        Args:
            size (int): Kvadratın ölçüsü.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
