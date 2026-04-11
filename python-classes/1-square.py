#!/usr/bin/python3
"""
Bu modul ölçüsü olan bir Square (Kvadrat) sinfini təyin edir.
"""


class Square:
    """
    Kvadratı təyin edən sinif.
    """

    def __init__(self, size):
        """
        Yeni bir Square instansiyasını (nümunəsini) yaradır.

        Args:
            size (int): Yeni kvadratın ölçüsü.
        """
        self.__size = size
