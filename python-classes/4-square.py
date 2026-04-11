#!/usr/bin/python3
"""
Bu modul Getter və Setter-i olan Square sinfini təyin edir.
"""


class Square:
    """
    Kvadratı təyin edən sinif.
    """

    def __init__(self, size=0):
        """
        Yeni bir Square yaradır.
        """
        self.size = size

    @property
    def size(self):
        """
        Gizli __size qiymətini götürmək üçün (getter).
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Gizli __size qiymətini təyin etmək üçün (setter).
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Kvadratın sahəsini qaytarır.
        """
        return self.__size ** 2
