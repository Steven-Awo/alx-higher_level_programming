#!/usr/bin/python3
'''Defining the class called Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''Representation of m rectangle.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializing a new width, height, x, y and id.'''
        super().__init__(id)
        self.width = width
        self.x = x
        self.height = height
        self.y = y

    @property
    def width(self):
        '''Setting/Getting the rectangle'dis width.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value


    @property
    def height(self):
        """Getting/setting the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """the x of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Getting/setting the y of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
