__init__.py
#!/usr/bin/python3
"""Defining the unittests for the base.py.

Unittest classes:
    TestBase_instantiation code - line 22
    TestBase_to_json_string code - line 108
    TestBase_save_to_file  code - line 154
    TestBase_from_json_string code - line 232
    TestBase_create code - line 286
    TestBase_load_from_file code - line 338
    TestBase_save_to_file_csv code - line 404
    TestBase_load_from_file_csv code - line 482
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittesting for testing of instantiation for the Base class."""

    def testing_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual( b2.id - 1, b1.id)

    def testing_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def testing_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def testing_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def testing_nb_instances_after_uniquee_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def testing_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def testing_nb_instancess_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def testing_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def testing_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def testing_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def testing_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def testing_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def testing_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def testing_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def testing_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def testing_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def testing_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def testing_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def testing_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def testing_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def testing_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def testing_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def testing_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for the testing of to_json_string method of the Base class."""

    def testing_to_json_string_rectangle_type(self):
        rc = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([rc.to_dictionary()])))

    def testing_to_json_string_rectangle_one_dict(self):
        rc = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([rc.to_dictionary()])) == 53)

    def testing_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def testing_to_json_string_square_type(self):
        sq = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))

    def testing_to_json_string_square_one_dict(self):
        sq = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([sq.to_dictionary()])) == 39)

    def testing_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def testing_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def testing_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def testing_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def testing_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for the testing of save_to_file method of the Base class."""

    @classmethod
    def tearDown(self):
        """Deleting any created file."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def testing_save_to_file_one_rectangle(self):
        rc = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rc])
        with open("Rectangle.json", "rc") as f:
            self.assertTrue(len(f.read()) == 53)

    def testing_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "rc") as f:
            self.assertTrue(len(f.read()) == 105)

    def testing_save_to_file_one_square(self):
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "rc") as f:
            self.assertTrue(len(f.read()) == 39)

    def testing_save_to_file_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "rc") as f:
            self.assertTrue(len(f.read()) == 77)

    def testing_save_to_file_cls_name_for_filename(self):
        sq = Square(10, 7, 2, 8)
        Base.save_to_file([sq])
        with open("Base.json", "rc") as f:
            self.assertTrue(len(f.read()) == 39)

    def testing_save_to_file_overwrite(self):
        sq = Square(9, 2, 39, 2)
        Square.save_to_file([sq])
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "rc") as f:
            self.assertTrue(len(f.read()) == 39)

    def testing_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "rc") as f:
            self.assertEqual("[]", f.read())

    def testing_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "rc") as f:
            self.assertEqual("[]", f.read())

    def testing_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def testing_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def testing_from_json_string_type(self):
        list_inputt = [{"id": 89, "width": 10, "height": 4}]
        json_lists_inputt = Rectangle.to_json_string(list_inputt)
        lists_outputt = Rectangle.from_json_string(json_lists_inputt)
        self.assertEqual(list, type(lists_outputt))

    def testing_from_json_string_one_rectangle(self):
        list_inputt = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_lists_inputt = Rectangle.to_json_string(list_inputt)
        lists_outputt = Rectangle.from_json_string(json_lists_inputt)
        self.assertEqual(list_inputt, lists_outputt)

    def testing_from_json_string_two_rectangles(self):
        list_inputt = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_lists_inputt = Rectangle.to_json_string(list_inputt)
        lists_outputt = Rectangle.from_json_string(json_lists_inputt)
        self.assertEqual(list_inputt, lists_outputt)

    def testing_from_json_string_one_square(self):
        list_inputt = [{"id": 89, "size": 10, "height": 4}]
        json_lists_inputt = Square.to_json_string(list_inputt)
        lists_outputt = Square.from_json_string(json_lists_inputt)
        self.assertEqual(list_inputt, lists_outputt)

    def testing_from_json_string_two_squares(self):
        list_inputt = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_lists_inputt = Square.to_json_string(list_inputt)
        lists_outputt = Square.from_json_string(json_lists_inputt)
        self.assertEqual(list_inputt, lists_outputt)

    def testing_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def testing_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def testing_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def testing_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unittests for the testing to create method of the Base class."""

    def testing_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def testing_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def testing_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def testing_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def testing_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def testing_create_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def testing_create_square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def testing_create_square_equals(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for the testing of load_from_file_method of the Base class."""

    @classmethod
    def tearDown(self):
        """Deleting any created file."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def testing_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectngles_outputt = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectngles_outputt[0]))

    def testing_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectngles_outputt = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectngles_outputt[1]))

    def testing_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        outputt = Rectangle.load_from_file()
        self.assertTrue(all(type(objj) == Rectangle for objj in outputt))

    def testing_load_from_file_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squars_outputt = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squars_outputt[0]))

    def testing_load_from_file_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squars_outputt = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squars_outputt[1]))

    def testing_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        outputt = Square.load_from_file()
        self.assertTrue(all(type(objj) == Square for objj in outputt))

    def testing_load_from_file_no_file(self):
        outputt = Square.load_from_file()
        self.assertEqual([], outputt)

    def testing_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for the testing of save_to_file_csv method of the Base class."""

    @classmethod
    def tearDown(self):
        """Deleting any created file."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def testing_save_to_file_csv_one_rectangle(self):
        rc = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([rc])
        with open("Rectangle.csv", "rc") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def testing_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "rc") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def testing_save_to_file_csv_one_square(self):
        sq = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "rc") as f:
            self.assertTrue("8,10,7,2", f.read())

    def testing_save_to_file_csv_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "rc") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def testing_save_to_file__csv_cls_name(self):
        sq = Square(10, 7, 2, 8)
        Base.save_to_file_csv([sq])
        with open("Base.csv", "rc") as f:
            self.assertTrue("8,10,7,2", f.read())

    def testing_save_to_file_csv_overwrite(self):
        sq = Square(9, 2, 39, 2)
        Square.save_to_file_csv([sq])
        sq = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "rc") as f:
            self.assertTrue("8,10,7,2", f.read())

    def testing_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "rc") as f:
            self.assertEqual("[]", f.read())

    def testing_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "rc") as f:
            self.assertEqual("[]", f.read())

    def testing_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def testing_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for the testing load_from_file_csv method of the Base class."""

    @classmethod
    def tearDown(self):
        """Deleting any created file."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def testing_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectngles_outputt = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectngles_outputt[0]))

    def testing_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectngles_outputt = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectngles_outputt[1]))

    def testing_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        outputt = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(objj) == Rectangle for objj in outputt))

    def testing_load_from_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squars_outputt = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squars_outputt[0]))

    def testing_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squars_outputt = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squars_outputt[1]))

    def testing_load_from_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        outputt = Square.load_from_file_csv()
        self.assertTrue(all(type(objj) == Square for objj in outputt))

    def testing_load_from_file_csv_no_file(self):
        outputt = Square.load_from_file_csv()
        self.assertEqual([], outputt)

    def testing_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
