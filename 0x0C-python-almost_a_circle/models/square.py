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
