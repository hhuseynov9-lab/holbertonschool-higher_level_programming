#!/usr/bin/python3
"""
Koordinatları və sahə hesablama qabiliyyəti olan Square sinfi.
"""


class Square:
    """
    Kvadratı təmsil edən sinif.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Yeni kvadrat yaradır.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Ölçünü götürür."""
        return self.__size

    @size.setter
    def size(self, value):
        """Ölçünü təyin edir və yoxlayır."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Koordinatları götürür."""
        return self.__position

    @position.setter
    def position(self, value):
        """Koordinatları təyin edir və yoxlayır."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Kvadratın sahəsini qaytarır."""
        return self.__size ** 2

    def my_print(self):
        """Kvadratı koordinatlara uyğun çap edir."""
        if self.__size == 0:
            print("")
            return

        # Y oxu (yuxarı boşluqlar)
        for i in range(self.__position[1]):
            print("")

        # Kvadratın özü və X oxu (sol boşluqlar)
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
