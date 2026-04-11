#!/usr/bin/python3
"""
Koordinatları olan Square sinfini təyin edən modul.
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
        """Ölçünü təyin edir."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Koordinatları götürür."""
        return self.__size_position  # Qeyd: burada ad __position olmalıdır

    @position.setter
    def position(self, value):
        """Koordinatları təyin edir və yoxlayır."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
