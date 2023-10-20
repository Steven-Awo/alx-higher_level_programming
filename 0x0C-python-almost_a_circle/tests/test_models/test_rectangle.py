#!/usr/bin/python3
'''Module for Rectangle unit tests.'''
import unittest
from models.base import Base
from random import randrange
from models.rectangle import Rectangle
from contextlib import redirect_stdout
import io


class TestRectangle(unittest.TestCase):
    '''Testing the the Base'ss class.'''

    def setsUp(self):
        '''Importing the module'ss instantiates class'''
        Base._Base__nb_objects = 0

    def tearsDown(self):
        '''Cleaning up everything after each of the testing_method.'''
        pass

    def testing_A_classs(self):
        '''Testing the Rectangle'ss class type.'''
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def testing_B_inheritancee(self):
        '''Testing the if Rectangle'ss inherits Base.'''
        self.assertTrue(issubclass(Rectangle, Base))

    def testing_C_constructorr_no_args(self):
        '''Testing the constructor'ss signature.'''
        with self.assertRaises(TypeError) as e:
            rr = Rectangle()
        ss = "__init__() missing 2 required positional arguments: 'width' \
and 'height'"
        self.assertEqual(str(e.exception), ss)

    def testing_C_constructorr_manyy_args(self):
        '''Testing the constructor's signature.'''
        with self.assertRaises(TypeError) as e:
            rr = Rectangle(1, 2, 3, 4, 5, 6)
        ss = "__init__() takes from 3 to 6 positional arguments but 7 were \
given"
        self.assertEqual(str(e.exception), ss)

    def testing_C_constructorr_one_args(self):
        '''Testing the constructor's signature.'''
        with self.assertRaises(TypeError) as e:
            rr = Rectangle(1)
        ss = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), ss)

    def testing_D_instantiationn(self):
        '''Testing the instantiations.'''
        rr = Rectangle(10, 20)
        self.assertEqual(str(type(rr)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(rr, Base))
        dd = {'_Rectangle__height': 20, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(rr.__dict__, dd)

        with self.assertRaises(TypeError) as e:
            rr = Rectangle("1", 2)
        msgg = "width must be an integer"
        self.assertEqual(str(e.exception), msgg)

        with self.assertRaises(TypeError) as e:
            rr = Rectangle(1, "2")
        msgg = "height must be an integer"
        self.assertEqual(str(e.exception), msgg)

        with self.assertRaises(TypeError) as e:
            rr = Rectangle(1, 2, "3")
        msgg = "x must be an integer"
        self.assertEqual(str(e.exception), msgg)

        with self.assertRaises(TypeError) as e:
            rr = Rectangle(1, 2, 3, "4")
        msgg = "y must be an integer"
        self.assertEqual(str(e.exception), msgg)

        with self.assertRaises(ValueError) as e:
            rr = Rectangle(-1, 2)
        msgg = "width must be > 0"
        self.assertEqual(str(e.exception), msgg)

        with self.assertRaises(ValueError) as e:
            rr = Rectangle(1, -2)
        msgg = "height must be > 0"
        self.assertEqual(str(e.exception), msgg)

        with self.assertRaises(ValueError) as e:
            rr = Rectangle(0, 2)
        msgg = "width must be > 0"
        self.assertEqual(str(e.exception), msgg)

        with self.assertRaises(ValueError) as e:
            rr = Rectangle(1, 0)
        msgg = "height must be > 0"
        self.assertEqual(str(e.exception), msgg)

        with self.assertRaises(ValueError) as e:
            rr = Rectangle(1, 2, -3)
        msgg = "x must be >= 0"
        self.assertEqual(str(e.exception), msgg)

        with self.assertRaises(ValueError) as e:
            rr = Rectangle(1, 2, 3, -4)
        msgg = "y must be >= 0"
        self.assertEqual(str(e.exception), msgg)

    def testing_D_instantiationn_positional(self):
        '''Testing the positional's instantiation.'''
        rr = Rectangle(5, 10, 15, 20)
        dd = {'_Rectangle__height': 10, '_Rectangle__width': 5,
             '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 1}
        self.assertEqual(rr.__dict__, dd)

        rr = Rectangle(5, 10, 15, 20, 98)
        dd = {'_Rectangle__height': 10, '_Rectangle__width': 5,
             '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 98}
        self.assertEqual(rr.__dict__, dd)

    def testing_D_instantiationn_keyword(self):
        '''Testing the positional's instantiation.'''
        rr = Rectangle(100, 200, id=421, y=99, x=101)
        dd = {'_Rectangle__height': 200, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(rr.__dict__, dd)

    def testing_E_id_inheritedd(self):
        '''Testing for if the id is to be inherited from the Base.'''
        Base._Base__nb_objects = 98
        rr = Rectangle(2, 4)
        self.assertEqual(rr.id, 99)

    def testing_F_propertiess(self):
        '''Testing the property's getters/setters.'''
        rr = Rectangle(5, 9)
        rr.width = 100
        rr.height = 101
        rr.x = 102
        rr.y = 103
        dd = {'_Rectangle__height': 101, '_Rectangle__width': 100,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(rr.__dict__, dd)
        self.assertEqual(rr.width, 100)
        self.assertEqual(rr.height, 101)
        self.assertEqual(rr.x, 102)
        self.assertEqual(rr.y, 103)


    def invalidd_types(self):
        '''Returning the tuple of types for the validation.'''
        tt = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
             [4], {5}, {6: 7}, None)
        return tt

    def testing_G_validatte_type(self):
        '''Testing the property's validation.'''
        rr = Rectangle(1, 2)
        attributess = ["x", "y", "width", "height"]
        for attribut in attributess:
            ss = "{} must be an integer".format(attribut)
            for invalid_typee in self.invalidd_types():
                with self.assertRaises(TypeError) as e:
                    setattr(rr, attribut, invalid_typee)
                self.assertEqual(str(e.exception), ss)

    def testing_G_validatew_value_negativee_gt(self):
        '''Testing the property's validation.'''
        rr = Rectangle(1, 2)
        attributess = ["width", "height"]
        for attribut in attributess:
            ss = "{} must be > 0".format(attribut)
            with self.assertRaises(ValueError) as e:
                setattr(rr, attribut, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), ss)

    def testing_G_validatee_value_negativee_ge(self):
        '''Testing the property's validation.'''
        rr = Rectangle(1, 2)
        attributess = ["x", "y"]
        for attribut in attributess:
            ss = "{} must be >= 0".format(attribut)
            with self.assertRaises(ValueError) as e:
                setattr(rr, attribut, -(randrange(10) + 1))
            self.assertEqual(str(e.exception), ss)

    def testing_G_validate_value_zero(self):
        '''Testing the property's validation.'''
        rr = Rectangle(1, 2)
        attributess = ["width", "height"]
        for attribut in attributess:
            ss = "{} must be > 0".format(attribut)
            with self.assertRaises(ValueError) as e:
                setattr(rr, attribut, 0)
            self.assertEqual(str(e.exception), ss)

    def testing_H_property(self):
        '''Testing the property's setting/getting.'''
        rr = Rectangle(1, 2)
        attributess = ["x", "y", "width", "height"]
        for attribut in attributess:
            n = randrange(10) + 1
            setattr(rr, attribut, n)
            self.assertEqual(getattr(rr, attribut), n)

    def testing_H_property_range_zero(self):
        '''Testing the property's setting/getting.'''
        rr = Rectangle(1, 2)
        rr.x = 0
        rr.y = 0
        self.assertEqual(rr.x, 0)
        self.assertEqual(rr.y, 0)

    def testing_I_areaa_no_args(self):
        '''Testing the area() method's signature.'''
        rr = Rectangle(5, 6)
        with self.assertRaises(TypeError) as e:
            Rectangle.area()
        ss = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), ss)

    def testing_I_area(self):
        '''Testing the area() method's compuation.'''
        rr = Rectangle(5, 6)
        self.assertEqual(rr.area(), 30)
        ww = randrange(10) + 1
        hh = randrange(10) + 1
        rr.width = ww
        rr.height = hh
        self.assertEqual(rr.area(), ww * hh)
        ww = randrange(10) + 1
        hh = randrange(10) + 1
        rr = Rectangle(ww, hh, 7, 8, 9)
        self.assertEqual(rr.area(), ww * hh)
        ww = randrange(10) + 1
        hh = randrange(10) + 1
        rr = Rectangle(ww, hh, y=7, x=8, id=9)
        self.assertEqual(rr.area(), ww * hh)

        rr1 = Rectangle(3, 2)
        self.assertEqual(rr1.area(), 6)

        rr2 = Rectangle(2, 10)
        self.assertEqual(rr2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def testing_J_displays_no_args(self):
        '''Testing the display() method's signature.'''
        rr = Rectangle(9, 8)
        with self.assertRaises(TypeError) as e:
            Rectangle.display()
        ss = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), ss)

    def testing_J_display_simple(self):
        '''Testing the display() method output.'''
        rr = Rectangle(1, 1)
        ff = io.StringIO()
        with redirect_stdout(ff):
            rr.display()
        ss = "#\n"
        self.assertEqual(ff.getvalue(), ss)
        rr.width = 3
        rr.height = 5
        ff = io.StringIO()
        with redirect_stdout(ff):
            rr.display()
        ss = "\
###\n\
###\n\
###\n\
###\n\
###\n\
"
        self.assertEqual(ff.getvalue(), ss)
        rr = Rectangle(5, 6, 7, 8)
        ff = io.StringIO()
        with redirect_stdout(ff):
            rr.display()
        ss = """







       #####
       #####
       #####
       #####
       #####
       #####
"""
        self.assertEqual(ff.getvalue(), ss)
        rr = Rectangle(9, 8)
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
"""
        self.assertEqual(ff.getvalue(), ss)
        rr = Rectangle(1, 1, 10, 10)
        ff = io.StringIO()
        with redirect_stdout(ff):
            rr.display()
        ss = """\










          #
"""
        self.assertEqual(ff.getvalue(), ss)

        rr = Rectangle(5, 5)
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

        rr = Rectangle(5, 3, 5)
        ff = io.StringIO()
        with redirect_stdout(ff):
            rr.display()
        ss = """\
     #####
     #####
     #####
"""
        self.assertEqual(ff.getvalue(), ss)

        rr = Rectangle(5, 3, 0, 4)
        ff = io.StringIO()
        with redirect_stdout(ff):
            rr.display()
        ss = """\




#####
#####
#####
"""
        self.assertEqual(ff.getvalue(), ss)

    def testing_K_strg_no_args(self):
        '''Testing the __str__() method's signature.'''
        rr = Rectangle(5, 2)
        with self.assertRaises(TypeError) as e:
            Rectangle.__str__()
        ss = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), ss)

    def testing_K_strg(self):
        '''Testing the __str__() method return.'''
        rr = Rectangle(5, 2)
        ss = '[Rectangle] (1) 0/0 - 5/2'
        self.assertEqual(str(rr), ss)
        rr = Rectangle(1, 1, 1)
        ss = '[Rectangle] (2) 1/0 - 1/1'
        self.assertEqual(str(rr), ss)
        rr = Rectangle(3, 4, 5, 6)
        ss = '[Rectangle] (3) 5/6 - 3/4'
        self.assertEqual(str(rr), ss)

        Base._Base__nb_objects = 0
        rr1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(rr1), "[Rectangle] (12) 2/1 - 4/6")

        rr2 = Rectangle(5, 5, 1)
        self.assertEqual(str(rr2), "[Rectangle] (1) 1/0 - 5/5")

    def testing_L_updatee_no_args(self):
        '''Testing the update() method's signature.'''
        rr = Rectangle(5, 2)
        with self.assertRaises(TypeError) as e:
            Rectangle.update()
        ss = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), ss)

        dd = rr.__dict__.copy()
        rr.update()
        self.assertEqual(rr.__dict__, dd)

    def testing_L_updatee_args(self):
        '''Testing the update() postional args.'''
        rr = Rectangle(5, 2)
        dd = rr.__dict__.copy()

        rr.update(10)
        dd["id"] = 10
        self.assertEqual(rr.__dict__, dd)

        rr.update(10, 5)
        dd["_Rectangle__width"] = 5
        self.assertEqual(rr.__dict__, dd)

        rr.update(10, 5, 17)
        dd["_Rectangle__height"] = 17
        self.assertEqual(rr.__dict__, dd)

        rr.update(10, 5, 17, 20)
        dd["_Rectangle__x"] = 20
        self.assertEqual(rr.__dict__, dd)

        rr.update(10, 5, 17, 20, 25)
        dd["_Rectangle__y"] = 25
        self.assertEqual(rr.__dict__, dd)

    def testing_L_updatee_args_bad(self):
        '''Testing the update() positional's arg fubars.'''
        rr = Rectangle(5, 2)
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
        ss = "height must be > 0"
        self.assertEqual(str(e.exception), ss)

        with self.assertRaises(ValueError) as e:
            rr.update(10, 5, 17, -20)
        ss = "x must be >= 0"
        self.assertEqual(str(e.exception), ss)

        with self.assertRaises(ValueError) as e:
            rr.update(10, 5, 17, 20, -25)
        ss = "y must be >= 0"
        self.assertEqual(str(e.exception), ss)

    def testing_L_updatee_kwargs(self):
        '''Testing the update()'s keyword args.'''
        rr = Rectangle(5, 2)
        dd = rr.__dict__.copy()

        rr.update(id=10)
        dd["id"] = 10
        self.assertEqual(rr.__dict__, dd)

        rr.update(width=5)
        dd["_Rectangle__width"] = 5
        self.assertEqual(rr.__dict__, dd)

        rr.update(height=17)
        dd["_Rectangle__height"] = 17
        self.assertEqual(rr.__dict__, dd)

        rr.update(x=20)
        dd["_Rectangle__x"] = 20
        self.assertEqual(rr.__dict__, dd)

        rr.update(y=25)
        dd["_Rectangle__y"] = 25
        self.assertEqual(rr.__dict__, dd)

    def testing_L_updatee_kwargs_2(self):
        '''Testing the update()'s keyword args.'''
        rr = Rectangle(5, 2)
        dd = rr.__dict__.copy()

        rr.update(id=10)
        dd["id"] = 10
        self.assertEqual(rr.__dict__, dd)

        rr.update(id=10, width=5)
        dd["_Rectangle__width"] = 5
        self.assertEqual(rr.__dict__, dd)

        rr.update(id=10, width=5, height=17)
        dd["_Rectangle__height"] = 17
        self.assertEqual(rr.__dict__, dd)

        rr.update(id=10, width=5, height=17, x=20)
        dd["_Rectangle__x"] = 20
        self.assertEqual(rr.__dict__, dd)

        rr.update(id=10, width=5, height=17, x=20, y=25)
        dd["_Rectangle__y"] = 25
        self.assertEqual(rr.__dict__, dd)

        rr.update(y=25, id=10, height=17, x=20, width=5)
        self.assertEqual(rr.__dict__, dd)

        Base._Base__nb_objects = 0
        rr1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rr1), "[Rectangle] (1) 10/10 - 10/10")

        rr1.update(height=1)
        self.assertEqual(str(rr1), "[Rectangle] (1) 10/10 - 10/1")

        rr1.update(width=1, x=2)
        self.assertEqual(str(rr1), "[Rectangle] (1) 2/10 - 1/1")

        rr1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(rr1), "[Rectangle] (89) 3/1 - 2/1")

        rr1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(rr1), "[Rectangle] (89) 1/3 - 4/2")

        Base._Base__nb_objects = 0
        rr1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rr1), "[Rectangle] (1) 10/10 - 10/10")

        rr1.update(89)
        self.assertEqual(str(rr1), "[Rectangle] (89) 10/10 - 10/10")

        rr1.update(89, 2)
        self.assertEqual(str(rr1), "[Rectangle] (89) 10/10 - 2/10")

        rr1.update(89, 2, 3)
        self.assertEqual(str(rr1), "[Rectangle] (89) 10/10 - 2/3")

        rr1.update(89, 2, 3, 4)
        self.assertEqual(str(rr1), "[Rectangle] (89) 4/10 - 2/3")

        rr1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rr1), "[Rectangle] (89) 4/5 - 2/3")

    def testing_M_too_dictionaryy(self):
        '''Testing the to_dictionary()'s signature:'''
        with self.assertRaises(TypeError) as e:
            Rectangle.to_dictionary()
        ss = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), ss)

        rr = Rectangle(1, 2)
        dd = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 2}
        self.assertEqual(rr.to_dictionary(), dd)

        rr = Rectangle(1, 2, 3, 4, 5)
        dd = {'x': 3, 'y': 4, 'width': 1, 'id': 5, 'height': 2}
        self.assertEqual(rr.to_dictionary(), dd)

        rr.x = 10
        rr.y = 20
        rr.width = 30
        rr.height = 40
        dd = {'x': 10, 'y': 20, 'width': 30, 'id': 5, 'height': 40}
        self.assertEqual(rr.to_dictionary(), dd)

        rr1 = Rectangle(10, 2, 1, 9)
        rr1_dictionaryy = rr1.to_dictionary()
        rr2 = Rectangle(1, 1)
        rr2.update(**rr1_dictionaryy)
        self.assertEqual(str(rr1), str(rr2))
        self.assertNotEqual(rr1, rr2)

if __name__ == "__main__":
    unittest.main()
