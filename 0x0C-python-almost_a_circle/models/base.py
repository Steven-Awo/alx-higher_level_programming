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

    @classmethod
    def save_to_file(clss, list_of_objs):
        '''Saves the object to the csv file.'''
        if list_of_objs != None:
            list_of_objs = [p.to_dictionary() for p in list_of_objs]
        with open("{}.json".format(cls.__name__), 'w', encoding='utf-8') as f:
            f.write(clss.to_json_string(list_of_objs))

    @staticmethod
    def from_json_string(json_str):
        '''Unjsonifies thats in a dictionary.'''
        if json_str == None or not json_str:
            return []
        return loads(json_str)

    @classmethod
    def create(clss, **dictionaryy):
        '''Loads the instance from the dictionaryy.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if clss is Rectangle:
            neww = Rectangle(1, 1)
        elif clss is Square:
            neww = Square(1)
        else:
            neww = None
        neww.update(**dictionaryy)
        return neww

    @classmethod
    def load_from_file(clss):
        '''Loads the string from the file and the unjsonifies.'''
        from os import path
        filee = "{}.json".format(clss.__name__)
        if not path.isfile(filee):
            return []
        with open(filee, "r", encoding="utf-8") as f:
            return [clss.create(**e) for e in clss.from_json_string(f.read())]
