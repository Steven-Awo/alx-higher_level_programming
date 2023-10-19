#!/usr/bin/python3
'''Defining the class called Base class.'''


class Base:
    '''Representation of a base of our own OOP hierarchy.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Initializing a new id.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
