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
        '''Rectangle's width.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validating_int("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Rectangle's height.'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validating_int("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''Rectangle's x.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validating_int("x", value, False)
        self.__x = value

    @property
    def y(self):
        '''Rectangle's y.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validating_int("y", value, False)
        self.__y = value

    def validating_int(self, name, value, eqq=True):
        '''Method for validating the value.'''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if eqq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eqq and value <= 0:
            raise ValueError("{} must be > 0".format(name))
