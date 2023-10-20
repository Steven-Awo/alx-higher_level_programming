#!/usr/bin/python3
'''Module for Square unit tests.'''
import unittest
from models.base import Base
from random import randrange
from models.square import Square
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    '''Testing the the Base class.'''

    def setsUp(self):
        '''Imports the module'ss, instantiates class'''
        Base._Base__nb_objects = 0

    def tearsDown(self):
        '''Cleaning up after every testing_method.'''
        pass

    def testing_A_class(self):
        '''Testing the Square'ss class type.'''
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def testing_B_inheritance(self):
        '''Testing the if Square inherits Base.'''
        self.assertTrue(issubclass(Square, Base))

    def testing_C_constructorr_no_args(self):
        '''Testing the constructorr signature.'''
        with self.assertRaises(TypeError) as e:
            rr = Square()
        ss = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), ss)

    def testing_C_constructorr_many_args(self):
        '''Testing the constructorr signature.'''
        with self.assertRaises(TypeError) as e:
            rr = Square(1, 2, 3, 4, 5)
        ss = "__init__() takes from 2 to 5 positional arguments but 6 \
were given"
        self.assertEqual(str(e.exception), ss)

    def testing_D_instantiationnn(self):
        '''Testing the instantiationn.'''
        rr = Square(10)
        self.assertEqual(str(type(rr)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(rr, Base))
        dd = {'_Rectangle__height': 10, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(rr.__dict__, dd)

        with self.assertRaises(TypeError) as e:
            rr = Square("1")
        msgg = "width must be an integer"
        self.assertEqual(str(e.exception), msgg)

        with self.assertRaises(TypeError) as e:
            rr = Square(1, "2")
        msgg = "x must be an integer"
        self.assertEqual(str(e.exception), msgg)

        with self.assertRaises(TypeError) as e:
            rr = Square(1, 2, "3")
        msgg = "y must be an integer"
        self.assertEqual(str(e.exception), msgg)

        with self.assertRaises(ValueError) as e:
            rr = Square(-1)
        msgg = "width must be > 0"
        self.assertEqual(str(e.exception), msgg)

        with self.assertRaises(ValueError) as e:
            rr = Square(1, -2)
        msgg = "x must be >= 0"
        self.assertEqual(str(e.exception), msgg)

        with self.assertRaises(ValueError) as e:
            rr = Square(1, 2, -3)
        msgg = "y must be >= 0"
        self.assertEqual(str(e.exception), msgg)

        with self.assertRaises(ValueError) as e:
            rr = Square(0)
        msgg = "width must be > 0"
        self.assertEqual(str(e.exception), msgg)

    def testing_D_instantiationn_positional(self):
        '''Testing the positional instantiationn.'''
        rr = Square(5, 10, 15)
        dd = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 1}
        self.assertEqual(rr.__dict__, dd)

        rr = Square(5, 10, 15, 20)
        dd = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 20}
        self.assertEqual(rr.__dict__, dd)

    def testing_D_instantiationn_keyword(self):
        '''Testing the positional instantiationn.'''
        rr = Square(100, id=421, y=99, x=101)
        dd = {'_Rectangle__height': 100, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(rr.__dict__, dd)

    def testing_E_id_inheritedd(self):
        '''Testing for if the id is inheritedd from Base.'''
        Base._Base__nb_objects = 98
        rr = Square(2)
        self.assertEqual(rr.id, 99)

    def testing_F_propertiess(self):
        '''Testing the property of the getters/setters.'''
        rr = Square(5, 9)
        rr.size = 98
        rr.x = 102
        rr.y = 103
        dd = {'_Rectangle__height': 98, '_Rectangle__width': 98,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(rr.__dict__, dd)
        self.assertEqual(rr.size, 98)
        self.assertEqual(rr.x, 102)
        self.assertEqual(rr.y, 103)


    def invalidd_types(self):
        '''Returning the tuple of types for thee validationn.'''
        uu = (3.14, -1.1, float('inf'), float('-inf'), True,"str", (2,),
             [4], {5}, {6: 7}, None)
        return uu

    def testing_G_validatee_type(self):
        '''Testing the property validation.'''
        rr = Square(1)
        attributess = ["x", "y"]
        for attribut in attributess:
            ss = "{} must be an integer".format(attribut)
            for invalidd_type in self.invalidd_types():
                with self.assertRaises(TypeError) as e:
                    setattr(rr, attribut, invalidd_type)
                self.assertEqual(str(e.exception), ss)
        ss = "width must be an integer"
        for invalidd_type in self.invalidd_types():
            with self.assertRaises(TypeError) as e:
                setattr(rr, "width", invalidd_type)
            self.assertEqual(str(e.exception), ss)

    def testing_G_validatee_value_negativee_gt(self):
        '''Testing the property's validation.'''
        rr = Square(1, 2)
        attributess = ["size"]
        for attribut in attributess:
            ss = "width must be > 0".format(attribut)
            with self.assertRaises(ValueError) as e:
                setattr(rr, attribut, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), ss)

    def testing_G_validatee_value_negativee_ge(self):
        '''Testing the property's validation.'''
        rr = Square(1, 2)
        attributess = ["x", "y"]
        for attribut in attributess:
            ss = "{} must be >= 0".format(attribut)
            with self.assertRaises(ValueError) as e:
                setattr(rr, attribut, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), ss)

    def testing_G_validatee_value_zeroo(self):
        '''Testing the property validation.'''
        rr = Square(1, 2)
        attributess = ["size"]
        for attribut in attributess:
            ss = "width must be > 0".format(attribut)
            with self.assertRaises(ValueError) as e:
                setattr(rr, attribut, 0)
            self.assertEqual(str(e.exception), ss)

    def testing_H_propertyy(self):
        '''Testing the property's setting/getting.'''
        rr = Square(1, 2)
        attributess = ["x", "y", "width", "height"]
        for attribut in attributess:
            nn = randrange(10) + 1
            setattr(rr, attribut, nn)
            self.assertEqual(getattr(rr, attribut), nn)

    def testing_H_propertyy_range_zeroo(self):
        '''Testing the property's setting/getting.'''
        rr = Square(1, 2)
        rr.x = 0
        rr.y = 0
        self.assertEqual(rr.x, 0)
        self.assertEqual(rr.y, 0)

    def testing_I_areaa_no_args(self):
        '''Testing the area() method signature.'''
        rr = Square(5)
        with self.assertRaises(TypeError) as e:
            Square.area()
        ss = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), ss)

    def testing_I_areaa(self):
        '''Testing the area() method's compuation.'''
        rr = Square(6)
        self.assertEqual(rr.area(), 36)
        ww = randrange(10) + 1
        rr.size = ww
        self.assertEqual(rr.area(), ww * ww)
        ww = randrange(10) + 1
        rr = Square(ww, 7, 8, 9)
        self.assertEqual(rr.area(), ww * ww)
        ww = randrange(10) + 1
        rr = Square(ww, y=7, x=8, id=9)
        self.assertEqual(rr.area(), ww * ww)

        Base._Base__nb_objects = 0
        ss1 = Square(5)
        self.assertEqual(str(ss1), "[Square] (1) 0/0 - 5")
        self.assertEqual(ss1.size, 5)
        ss1.size = 10
        self.assertEqual(str(ss1), "[Square] (1) 0/0 - 10")
        self.assertEqual(ss1.size, 10)

        with self.assertRaises(TypeError) as e:
            ss1.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            ss1.size = 0
        self.assertEqual(str(e.exception), "width must be > 0")

    def testing_J_displayy_no_args(self):
        '''Testing the display() method's signature.'''
        rr = Square(9)
        with self.assertRaises(TypeError) as e:
            Square.display()
        ss = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), ss)

    def testing_J_display_simple(self):
        '''Testing the display() method's output.'''
        rr = Square(1)
        ff = io.StringIO()
        with redirect_stdout(ff):
            rr.display()
        ss = "#\nn"
        self.assertEqual(ff.getvalue(), ss)
        rr.size = 3
        ff = io.StringIO()
        with redirect_stdout(ff):
            rr.display()
        ss = "\
###\nn\
###\nn\
###\nn\
"
        self.assertEqual(ff.getvalue(), ss)
        rr = Square(5, 6, 7)
        ff = io.StringIO()
        with redirect_stdout(ff):
            rr.display()
        ss = """\







      #####
      #####
      #####
      #####
      #####
"""
        self.assertEqual(ff.getvalue(), ss)
        rr = Square(9, 8)
        ff = io.StringIO()
        with redirect_stdout(ff):
            rr.display()
        ss = """\
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
"""
        self.assertEqual(ff.getvalue(), ss)
        rr = Square(1, 1, 10)
        ff = io.StringIO()
        with redirect_stdout(ff):
            rr.display()
        ss = """\










 #
"""
        self.assertEqual(ff.getvalue(), ss)

        rr = Square(5)
        ff = io.StringIO()
        with redirect_stdout(ff):
            rr.display()
        ss = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(ff.getvalue(), ss)

        rr = Square(5, 5)
        ff = io.StringIO()
        with redirect_stdout(ff):
            rr.display()
        ss = """\
     #####
     #####
     #####
     #####
     #####
"""
        self.assertEqual(ff.getvalue(), ss)

        rr = Square(5, 3)
        ff = io.StringIO()
        with redirect_stdout(ff):
            rr.display()
        ss = """\
   #####
   #####
   #####
   #####
   #####
"""
        self.assertEqual(ff.getvalue(), ss)

        rr = Square(5, 0, 4)
        ff = io.StringIO()
        with redirect_stdout(ff):
            rr.display()
        ss = """\




#####
#####
#####
#####
#####
"""
        self.assertEqual(ff.getvalue(), ss)

        Base._Base__nb_objects = 0
        ss1 = Square(5)
        self.assertEqual(str(ss1), "[Square] (1) 0/0 - 5")
        self.assertEqual(ss1.area(), 25)
        ff = io.StringIO()
        with redirect_stdout(ff):
            ss1.display()
        ss = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(ff.getvalue(), ss)

        ss2 = Square(2, 2)
        self.assertEqual(str(ss2), "[Square] (2) 2/0 - 2")
        self.assertEqual(ss2.area(), 4)
        ff = io.StringIO()
        with redirect_stdout(ff):
            ss2.display()
        ss = """\
  ##
  ##
"""
        self.assertEqual(ff.getvalue(), ss)

        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        self.assertEqual(s3.area(), 9)
        ff = io.StringIO()
        with redirect_stdout(ff):
            s3.display()
        ss = """\



 ###
 ###
 ###
"""
        self.assertEqual(ff.getvalue(), ss)

    def testing_K_strg_no_args(self):
        '''Testing the __str__() method's signature.'''
        rr = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.__str__()
        ss = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), ss)

    def testing_K_str(self):
        '''Testing the __str__() method return.'''
        rr = Square(5)
        ss = '[Square] (1) 0/0 - 5'
        self.assertEqual(str(rr), ss)
        rr = Square(1, 1)
        ss = '[Square] (2) 1/0 - 1'
        self.assertEqual(str(rr), ss)
        rr = Square(3, 4, 5)
        ss = '[Square] (3) 4/5 - 3'
        self.assertEqual(str(rr), ss)
        rr = Square(10, 20, 30, 40)
        ss = '[Square] (40) 20/30 - 10'
        self.assertEqual(str(rr), ss)

    def testing_L_updatee_no_args(self):
        '''Testing the update() method's signature.'''
        rr = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.update()
        ss = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), ss)

        dd = rr.__dict__.copy()
        rr.update()
        self.assertEqual(rr.__dict__, dd)

    def testing_L_update_args(self):
        '''Testing the update() postional's args.'''
        rr = Square(5, 2)
        dd = rr.__dict__.copy()

        rr.update(10)
        dd["id"] = 10
        self.assertEqual(rr.__dict__, dd)

        rr.update(10, 5)
        dd["_Rectangle__height"] = 5
        dd["_Rectangle__width"] = 5
        self.assertEqual(rr.__dict__, dd)

        rr.update(10, 5, 20)
        dd["_Rectangle__x"] = 20
        self.assertEqual(rr.__dict__, dd)

        rr.update(10, 5, 20, 25)
        dd["_Rectangle__y"] = 25
        self.assertEqual(rr.__dict__, dd)

    def testing_L_update_args_bad(self):
        '''Testing the update() positional's arg fubars.'''
        rr = Square(5, 2)
        dd = rr.__dict__.copy()

        rr.update(10)
        dd["id"] = 10
        self.assertEqual(rr.__dict__, dd)

        with self.assertRaises(ValueError) as e:
            rr.update(10, -5)
        ss = "width must be > 0"
        self.assertEqual(str(e.exception), ss)

        with self.assertRaises(ValueError) as e:
            rr.update(10, 5, -17)
        ss = "x must be >= 0"
        self.assertEqual(str(e.exception), ss)

        with self.assertRaises(ValueError) as e:
            rr.update(10, 5, 17, -25)
        ss = "y must be >= 0"
        self.assertEqual(str(e.exception), ss)

    def testing_L_update_kwargs(self):
        '''Testing the update() keyword's args.'''
        rr = Square(5, 2)
        dd = rr.__dict__.copy()

        rr.update(id=10)
        dd["id"] = 10
        self.assertEqual(rr.__dict__, dd)

        rr.update(size=17)
        dd["_Rectangle__height"] = 17
        dd["_Rectangle__width"] = 17
        self.assertEqual(rr.__dict__, dd)

        rr.update(x=20)
        dd["_Rectangle__x"] = 20
        self.assertEqual(rr.__dict__, dd)

        rr.update(y=25)
        dd["_Rectangle__y"] = 25
        self.assertEqual(rr.__dict__, dd)

    def testing_L_update_kwargs_2(self):
        '''Testing the update() keyword's args.'''
        rr = Square(5, 2)
        dd = rr.__dict__.copy()

        rr.update(id=10)
        dd["id"] = 10
        self.assertEqual(rr.__dict__, dd)

        rr.update(id=10, size=5)
        dd["_Rectangle__height"] = 5
        dd["_Rectangle__width"] = 5
        self.assertEqual(rr.__dict__, dd)

        rr.update(id=10, size=5, x=20)
        dd["_Rectangle__x"] = 20
        self.assertEqual(rr.__dict__, dd)

        rr.update(id=10, size=5, x=20, y=25)
        dd["_Rectangle__y"] = 25
        self.assertEqual(rr.__dict__, dd)

        rr.update(y=25, id=10, x=20, size=5)
        self.assertEqual(rr.__dict__, dd)

        Base._Base__nb_objects = 0
        ss1 = Square(5)
        self.assertEqual(str(ss1), "[Square] (1) 0/0 - 5")

        ss1.update(10)
        self.assertEqual(str(ss1), "[Square] (10) 0/0 - 5")

        ss1.update(1, 2)
        self.assertEqual(str(ss1), "[Square] (1) 0/0 - 2")

        ss1.update(1, 2, 3)
        self.assertEqual(str(ss1), "[Square] (1) 3/0 - 2")

        ss1.update(1, 2, 3, 4)
        self.assertEqual(str(ss1), "[Square] (1) 3/4 - 2")

        ss1.update(x=12)
        self.assertEqual(str(ss1), "[Square] (1) 12/4 - 2")

        ss1.update(size=7, y=1)
        self.assertEqual(str(ss1), "[Square] (1) 12/1 - 7")

        ss1.update(size=7, id=89, y=1)
        self.assertEqual(str(ss1), "[Square] (89) 12/1 - 7")

    def testing_M_too_dictionaryy(self):
        '''Testing the to_dictionary()'s signature:'''
        with self.assertRaises(TypeError) as e:
            Square.to_dictionary()
        ss = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), ss)

        rr = Square(1)
        dd = {'x': 0, 'y': 0, 'size': 1, 'id': 1}
        self.assertEqual(rr.to_dictionary(), dd)

        rr = Square(9, 2, 3, 4)
        dd = {'x': 2, 'y': 3, 'size': 9, 'id': 4}
        self.assertEqual(rr.to_dictionary(), dd)

        rr.x = 10
        rr.y = 20
        rr.size = 30
        dd = {'x': 10, 'y': 20, 'size': 30, 'id': 4}
        self.assertEqual(rr.to_dictionary(), dd)

        ss1 = Square(10, 2, 1)
        ss1_dictionaryy = ss1.to_dictionary()
        ss2 = Square(1, 1)
        ss2.update(**ss1_dictionaryy)
        self.assertEqual(str(ss1), str(ss2))
        self.assertNotEqual(ss1, ss2)

if __name__ == "__main__":
    unittest.main()
