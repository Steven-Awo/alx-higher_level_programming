#!/usr/bin/python3
'''Module for Base unit testing.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Testing the Base't class.'''

    def setUp(self):
        '''Importing the module, the instantiates of class'''
        Base._Base__nb_objects = 0
        pass

    def tearsDown(self):
        '''Cleaning up after each of the testing_method.'''
        pass

    def testing_A_nbb_objets_private(self):
        '''Testing if  the nb_objects is a private class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def testing_B_nbb_objets_initialized(self):
        '''Testing if the nb_objects has initialized to zero.'''
        self.assertEqual(getattr(Base, "_Base__nbb_objects"), 0)

    def testing_C_instantiationn(self):
        '''Testing the Base()'t instantiation.'''
        be = Base()
        self.assertEqual(str(type(be)), "<class 'models.base.Base'>")
        self.assertEqual(be.__dict__, {"id": 1})
        self.assertEqual(be.id, 1)

    def testing_D_constructorr(self):
        '''Testing the constructor't signature.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msgg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msgg)

    def testing_D_constructorr_args_2(self):
        '''Testing constructor signature with 2 notself args.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msgg = "__init__() takes from 1 to 2 positional arguments but 3\
were given"
        self.assertEqual(str(e.exception), msgg)

    def testing_E_consecutivee_ids(self):
        '''Testing the consecutive't ids.'''
        bb1 = Base()
        bb2 = Base()
        self.assertEqual(bb1.id + 1, bb2.id)

    def testing_F_id_syncedd(self):
        '''Testing the sync between the class and the instance id.'''
        be = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), be.id)

    def testing_F_id_syncedd_more(self):
        '''Testing the syncing between the class and the instance id.'''
        be = Base()
        be = Base("Foo")
        be = Base(98)
        be = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), be.id)

    def testing_G_customm_id_int(self):
        '''Testing the customized int id.'''
        x = 98
        be = Base(x)
        self.assertEqual(be.id, x)

    def testing_G_customm_id_str(self):
        '''Testing the customized int id.'''
        x = "FooBar"
        be = Base(x)
        self.assertEqual(be.id, x)

    def testing_G_id_keywordd(self):
        '''Testing the id passed as a keyword arg.'''
        x = 421
        be = Base(id=x)
        self.assertEqual(be.id, x)

    def testing_H_too_jsonn_string(self):
        '''Testing the to_json_string()'t signature:'''
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        t = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(e.exception), t)

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]

        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))

        d = [{"foobarroooo": 98989898}, {"abc": 123}, {"HI": 0}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"foobarroooo": 98989898}, {"abc": 123}, {"HI": 0}]')

        d = [{"foobarroooo": 98989898}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"foobarroooo": 98989898}]')

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}]')
        d = [{}, {}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}, {}]')

        rr1 = Rectangle(10, 7, 2, 8)
        dictionaryy = rr1.to_dictionary()
        json_dictionaryy = Base.to_json_string([dictionaryy])
        dictionaryy = str([dictionaryy])
        dictionaryy = dictionaryy.replace("'", '"')
        self.assertEqual(dictionaryy, json_dictionaryy)

        rr1 = Rectangle(10, 7, 2, 8)
        rr2 = Rectangle(1, 2, 3, 4)
        rr3 = Rectangle(2, 3, 4, 5)
        dictionaryy = [rr1.to_dictionary(), rr2.to_dictionary(),
                      rr3.to_dictionary()]
        json_dictionaryy = Base.to_json_string(dictionaryy)
        dictionaryy = str(dictionaryy)
        dictionaryy = dictionaryy.replace("'", '"')
        self.assertEqual(dictionaryy, json_dictionaryy)

        rr1 = Square(10, 7, 2)
        dictionaryy = rr1.to_dictionary()
        json_dictionaryy = Base.to_json_string([dictionaryy])
        dictionaryy = str([dictionaryy])
        dictionaryy = dictionaryy.replace("'", '"')
        self.assertEqual(dictionaryy, json_dictionaryy)

        rr1 = Square(10, 7, 2)
        rr2 = Square(1, 2, 3)
        rr3 = Square(2, 3, 4)
        dictionaryy = [rr1.to_dictionary(), rr2.to_dictionary(),
                      rr3.to_dictionary()]
        json_dictionaryy = Base.to_json_string(dictionaryy)
        dictionaryy = str(dictionaryy)
        dictionaryy = dictionaryy.replace("'", '"')
        self.assertEqual(dictionaryy, json_dictionaryy)

    def testing_H_testing_from_json_stringg(self):
        '''Testing the to_json_string()'s signature:'''
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        t = "from_json_string() missing 1 required positional argument: \
'json_string'"
        self.assertEqual(str(e.exception), t)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        t = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, \
{"x": 101, "y": 20123, "width": 312321, "id": 522244, "height": 34340}]'
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(Base.from_json_string(t), d)

        d = [{}, {}]
        t = '[{}, {}]'
        self.assertEqual(Base.from_json_string(t), d)
        d = [{}]
        t = '[{}]'
        self.assertEqual(Base.from_json_string(t), d)

        d = [{"foobarroooo": 98989898}, {"abc": 123}, {"HI": 0}]
        t = '[{"foobarroooo": 98989898}, {"abc": 123}, {"HI": 0}]'
        self.assertEqual(Base.from_json_string(t), d)

        d = [{"foobarroooo": 98989898}]
        t = '[{"foobarroooo": 98989898}]'
        self.assertEqual(Base.from_json_string(t), d)

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        t = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.from_json_string(t), d)

        d = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        t = '[{"x": 101, "y": 20123, "width": 312321, "id": 522244, \
"height": 34340}]'
        self.assertEqual(Base.from_json_string(t), d)

        listt_in = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        listt_out = Rectangle.from_json_string(
            Rectangle.to_json_string(listt_in))
        self.assertEqual(listt_in, listt_out)

    def testing_I_save_to_file(self):
        '''Testing the save_to_file()'s method.'''
        import os
        rr1 = Rectangle(10, 7, 2, 8)
        rr2 = Rectangle(2, 4)
        Rectangle.save_to_file([rr1, rr2])

        with open("Rectangle.json", "r") as filee:
            self.assertEqual(len(filee.read()), 105)


        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as filee:
            self.assertEqual(filee.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as filee:
            self.assertEqual(filee.read(), "[]")

        rr2 = Rectangle(2, 4)
        Rectangle.save_to_file([rr2])
        with open("Rectangle.json", "r") as filee:
            self.assertEqual(len(filee.read()), 52)

        Square.save_to_file(None)
        with open("Square.json", "r") as filee:
            self.assertEqual(filee.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as filee:
            self.assertEqual(filee.read(), "[]")

        rr2 = Square(1)
        Square.save_to_file([rr2])
        with open("Square.json", "r") as filee:
            self.assertEqual(len(filee.read()), 38)


    def testing_J_createe(self):
        '''Testing the create()'s method.'''
        rr1 = Rectangle(3, 5, 1)
        r1_dictionary = rr1.to_dictionary()
        rr2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(rr1), str(rr2))
        self.assertFalse(rr1 is rr2)
        self.assertFalse(rr1 == rr2)

    def testing_K_loadd_from_filee(self):
        '''Testing the load_from_file()'s method.'''
        rr1 = Rectangle(10, 7, 2, 8)
        rr2 = Rectangle(2, 4)
        listt_in = [rr1, rr2]
        Rectangle.save_to_file(listt_in)
        listt_out = Rectangle.load_from_file()
        self.assertNotEqual(id(listt_in[0]), id(listt_out[0]))
        self.assertEqual(str(listt_in[0]), str(listt_out[0]))
        self.assertNotEqual(id(listt_in[1]), id(listt_out[1]))
        self.assertEqual(str(listt_in[1]), str(listt_out[1]))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        listt_in = [s1, s2]
        Square.save_to_file(listt_in)
        listt_out = Square.load_from_file()
        self.assertNotEqual(id(listt_in[0]), id(listt_out[0]))
        self.assertEqual(str(listt_in[0]), str(listt_out[0]))
        self.assertNotEqual(id(listt_in[1]), id(listt_out[1]))
        self.assertEqual(str(listt_in[1]), str(listt_out[1]))

if __name__ == "__main__":
    unittest.main()
