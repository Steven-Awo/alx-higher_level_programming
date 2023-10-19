#!/usr/bin/python3
'''Defining the class called Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Representing of the square class class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initializing a new size, x, y and id.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returning the info about the string as a string.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)
