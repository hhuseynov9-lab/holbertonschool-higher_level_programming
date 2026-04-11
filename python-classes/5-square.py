#!/usr/bin/python3
"""
Kvadratı çap etmək imkanı olan Square sinfi.
"""


class Square:
    """
    Kvadratı təyin edən sinif.
    """

    def __init__(self, size=0):
        """
        Yeni kvadrat yaradır.
        """
        self.size = size

    @property
    def size(self):
        """
        Ölçünü götürür.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Ölçünü təyin edir və yoxlayır.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Sahəni hesablayır.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Kvadratı '#' simvolu ilə standart çıxışa (stdout) çap edir.
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
