#!/usr/bin/python3
'''Defining the class called Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''Representation of m rectangle.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializing a new width, height, x, y and id.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''rectangle's width.'''
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        if value < 0 or value == 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''rectangle's height.'''
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        if value < 0 and value == 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        '''rectangle's x.'''
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("x must be an integer")
        if value < 0 and value == 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''rectangle's y.'''
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("y must be an integer")
        if value < 0 and value == 0:
            raise ValueError("y must be >= 0")
        self.__y = value
