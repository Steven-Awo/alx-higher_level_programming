#!/usr/bin/python3
'''Module for the class called Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Representing of a Square class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initializing a new size, x, y and id.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returning the info about the square as a string.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.height)

    @property
    def size(self):
        '''Square's size.'''
        return self.height

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value
