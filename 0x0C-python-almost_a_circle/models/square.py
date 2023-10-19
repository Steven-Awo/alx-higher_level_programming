#!/usr/bin/python3
'''Defining the class called Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Representing of the square class class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returning the string info about a square.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Square's size.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal's method that updates the instance's attributes
        via */**args.'''
        if id != None:
            self.id = id
        if size != None:
            self.width = size
        if x != None:
            self.x = x
        if y != None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updating the instance's attributes via the no-keyword & the
        keyword args.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
