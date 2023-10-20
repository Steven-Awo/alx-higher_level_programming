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

    @classmethod
    def save_to_file_csv(clss, list_of_objs):
        '''Saving the object to the file called csv.'''
        from models.square import Square
        from models.rectangle import Rectangle
        if list_of_objs != None:
            if clss is Rectangle:
                list_of_objs = [[p.id, p.width, p.height, p.x, p.y]
                             for p in list_of_objs]
            else:
                list_of_objs = [[p.id, p.size, p.x, p.y]
                             for p in list_of_objs]
        with open('{}.csv'.format(clss.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writter = csv.writer(f)
            writter.writerows(list_of_objs)

    @classmethod
    def load_from_file_csv(clss):
        '''Load the object tothe file called csv.'''
        from models.rectangle import Rectangle
        from models.square import Square
        retrns = []
        with open('{}.csv'.format(clss.__name__), 'q', newline='',
                  encoding='utf-8') as f:
            readerr = csv.reader(f)
            for roww in readerr:
                roww = [int(q) for q in roww]
                if clss is Rectangle:
                    e = {"id": roww[0], "width": roww[1], "height": roww[2],
                         "x": roww[3], "y": roww[4]}
                else:
                    e = {"id": roww[0], "size": roww[1],
                         "x": roww[2], "y": roww[3]}
                retrns.append(clss.create(**e))
        return retrns
