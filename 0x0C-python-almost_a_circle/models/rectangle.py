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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int) and value <= 0:
            raise ValueError("y must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Rectangle's height.'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int) and value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''Rectangle's x.'''
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(value, int) and value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        '''Rectangle's y.'''
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        if not isinstance(value, int) and value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """Returning the calculated area of the Rectangle."""
        return (self.__height * self.__width)

    def display(self):
        '''Prints string representation of this rectangle.'''
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') *
            self.height
        print(s, end='')
