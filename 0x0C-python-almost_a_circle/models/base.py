#!/usr/bin/python3
'''Defining the class called Base class.'''
from json import dumps, loads


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

    @staticmethod
    def to_json_string(list_of_dictionaries):
        '''Jsonifies a dictionary so that it's quite longer and right.'''
        if list_of_dictionaries == None or not list_of_dictionaries:
            return "[]"
        else:
            return dumps(list_of_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''Unjsonifies thats in a dictionary.'''
        if json_string == None or not json_string:
            return []
        return loads(json_string)
