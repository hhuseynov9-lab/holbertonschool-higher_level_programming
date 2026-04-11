#!/usr/bin/python3
'''
ff
'''
class Square:
    '''
    f
    '''

    def __init__(self, size=0):
       '''
       f
       '''
        if type(size)  is not int:
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
       '''
       f
       '''
        self.size = size * size
    
    self.__size
