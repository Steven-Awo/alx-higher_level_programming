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
        x = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(x, end='')

    def __str__(self):
        '''Returns string info about this rectangle.'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Internal's method that updates the instance's attributes
        via */**args.'''
        if id != None:
            self.id = id
        if width != None:
            self.width = width
        if height != None:
            self.height = height
        if x != None:
            self.x = x
        if y != None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updating the instance's attributes via the no-keyword & the keyword
        args.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returning the dictionary's representation of a class.'''
        return {"id": self.id,"width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
