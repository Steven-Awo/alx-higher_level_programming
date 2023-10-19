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
        '''TSetting/Getting the rectangle'dis width.'''
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        """Getting/setting the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """Getting/setting the x of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getting/setting the y of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__x = value

    def area(self):
        """Returning the calculated area of the Rectangle."""
        return (self.__height * self.__width)

    def display(self):
        '''Printing the string's representation of the rectangle.'''
        dis = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * \
                self.height
        print(dis, end='')

    def __str__(self):
        '''Returns the info of the rectangle in string.'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y,
                   self.width, self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Internal's method that does update the instance's attributes via
        */**args.'''
        if id is not None:
            self.id = id
        if x is not None:
            self.x = x
        if width is not None:
            self.width = width
        if y is not None:
            self.y = y
        if height is not None:
            self.height = height

    def update(self, *args, **kwargs):
        '''Updates the instance's attributes via the no-keyword &
        the keyword args.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns the dictionary's representation of the class.'''
        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.__x, "y": self.__y}
