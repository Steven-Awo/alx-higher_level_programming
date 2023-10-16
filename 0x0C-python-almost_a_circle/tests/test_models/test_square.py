#!/usr/bin/python3
"""Defines unittests for models/square.py.

Unittest classes:
    TestSquare_instantiation - line 26
    TestSquare_size - line 90
    TestSquare_x - line 167
    TestSquare_y - line 239
    TestSquare_order_of_initialization - line 307
    TestSquare_area - line 323
    TestSquare_stdout - line 345
    TestSquare_update_args - line 427
    TestSquare_update_kwargs - line 539
    TestSquare_to_dictionary - 641
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for the testing of instantiation of the Square's class."""

    def testing_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def testing_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def testing_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def testing_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def testing_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def testing_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def testing_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def testing_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def testing_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def testing_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def testing_size_setter(self):
        sq = Square(4, 1, 9, 2)
        sq.size = 8
        self.assertEqual(8, sq.size)

    def testing_width_getter(self):
        sq = Square(4, 1, 9, 2)
        sq.size = 8
        self.assertEqual(8, sq.width)

    def testing_height_getter(self):
        sq = Square(4, 1, 9, 2)
        sq.size = 8
        self.assertEqual(8, sq.height)

    def testing_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def testing_y_getter(self):
        self.assertEqual(0, Square(10).y)


class TestSquare_size(unittest.TestCase):
    """Unittests for the testing size the initialization of the
    Square's class."""

    def testing_None_size(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square(None)

    def testing_str_size(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square("invalid")

    def testing_float_size(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square(5.5)

    def testing_complex_size(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square(complex(5))

    def testing_dict_size(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def testing_bool_size(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square(True, 2, 3)

    def testing_list_size(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square([1, 2, 3])

    def testing_set_size(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square({1, 2, 3}, 2)

    def testing_tuple_size(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def testing_frozenset_size(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    def testing_range_size(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square(range(5))

    def testing_bytes_size(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square(b'Python')

    def testing_bytearray_size(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square(bytearray(b'abcdefg'))

    def testing_memoryview_size(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square(memoryview(b'abcdefg'))

    def testing_inf_size(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square(float('inf'))

    def testing_nan_size(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square(float('nan'))

    # Test size values
    def testing_negative_size(self):
        with self.assertRaisesRegex(ValueError,
                "width must be > 0"):
            Square(-1, 2)

    def testing_zero_size(self):
        with self.assertRaisesRegex(ValueError,
                "width must be > 0"):
            Square(0, 2)

class TestSquare_x(unittest.TestCase):
    """Unittests for the testing of initialization of Square's x attribute."""

    def testing_None_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Square(1, None)

    def testing_str_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Square(1, "invalid")

    def testing_float_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Square(1, 5.5)

    def testing_complex_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Square(1, complex(5))

    def testing_dict_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)

    def testing_bool_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Square(1, True)

    def testing_list_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Square(1, [1, 2, 3])

    def testing_set_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Square(1, {1, 2, 3})

    def testing_tuple_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Square(1, (1, 2, 3))

    def testing_frozenset_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Square(1, frozenset({1, 2, 3, 1}))

    def testing_range_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Square(1, range(5))

    def testing_bytes_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Square(1, b'Python')

    def testing_bytearray_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Square(1, bytearray(b'abcdefg'))

    def testing_memoryview_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Square(1, memoryview(b'abcedfg'))

    def testing_inf_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Square(1, float('inf'), 2)

    def testing_nan_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Square(1, float('nan'), 2)

    def testing_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)


class TestSquare_y(unittest.TestCase):
    """Unittests for the testing of initialization of Square's y attribute."""

    def testing_None_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Square(1, 3, None)

    def testing_str_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Square(1, 1, "invalid")

    def testing_float_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Square(1, 3, 5.5)

    def testing_complex_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Square(1, 3, complex(5))

    def testing_dict_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Square(1, 1, {"a": 1, "b": 2})

    def testing_list_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Square(1, 1, [1, 2, 3])

    def testing_set_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Square(1, 1, {1, 2, 3})

    def testing_tuple_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Square(1, 1, (1, 2, 3))

    def testing_frozenset_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Square(1, 3, frozenset({1, 2, 3, 1}))

    def testing_range_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Square(1, 3, range(5))

    def testing_bytes_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Square(1, 3, b'Python')

    def testing_bytearray_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Square(1, 3, bytearray(b'abcdefg'))

    def testing_memoryview_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Square(1, 3, memoryview(b'abcedfg'))

    def testing_inf_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Square(1, 1, float('inf'))

    def testing_nan_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Square(1, 1, float('nan'))

    def testing_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)


class TestSquare_order_of_initialization(unittest.TestCase):
    """Unittests for the testing of order of Square's attribute initialization."""

    def testing_size_before_x(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square("invalid size", "invalid x")

    def testing_size_before_y(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    def testing_x_before_y(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Square(1, "invalid x", "invalid y")


class TestSquare_area(unittest.TestCase):
    """Unittests for the testing of the area method of the Square's class."""

    def testing_area_small(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def testing_area_large(self):
        sq = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, sq.area())

    def testing_area_changed_attributes(self):
        sq = Square(2, 0, 0, 1)
        sq.size = 7
        self.assertEqual(49, sq.area())

    def testing_area_one_arg(self):
        sq = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            sq.area(1)


class TestSquare_stdout(unittest.TestCase):
    """Unittests for the testing __str__ and the display methods of
    Square class."""

    @staticmethod
    def capture_stdout(sq, method):
        """Capturing and returning the text printed to the stdout.

        Args:
            sq (Square): The Square ot to be printed to stdout.
            method (str): The method to be runned on the sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capturee = io.StringIO()
        sys.stdout = capturee
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capturee

    def testing_str_method_print_size(self):
        sq = Square(4)
        capturee = TestSquare_stdout.capture_stdout(sq, "print")
        correctt = "[Square] ({}) 0/0 - 4\n".format(sq.id)
        self.assertEqual(correctt, capturee.getvalue())

    def testing_str_method_size_x(self):
        sq = Square(5, 5)
        correctt = "[Square] ({}) 5/0 - 5".format(sq.id)
        self.assertEqual(correctt, sq.__str__())

    def testing_str_method_size_x_y(self):
        sq = Square(7, 4, 22)
        correctt = "[Square] ({}) 4/22 - 7".format(sq.id)
        self.assertEqual(correctt, str(sq))

    def testing_str_method_size_x_y_id(self):
        sq = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(sq))

    def testing_str_method_changed_attributes(self):
        sq = Square(7, 0, 0, [4])
        sq.size = 15
        sq.x = 8
        sq.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(sq))

    def testing_str_method_one_arg(self):
        sq = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            sq.__str__(1)

    # Test display method
    def testing_display_size(self):
        sq = Square(2, 0, 0, 9)
        capturee = TestSquare_stdout.capture_stdout(sq, "display")
        self.assertEqual("##\n##\n", capturee.getvalue())

    def testing_display_size_x(self):
        sq = Square(3, 1, 0, 18)
        capturee = TestSquare_stdout.capture_stdout(sq, "display")
        self.assertEqual(" ###\n ###\n ###\n", capturee.getvalue())

    def testing_display_size_y(self):
        sq = Square(4, 0, 1, 9)
        capturee = TestSquare_stdout.capture_stdout(sq, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capturee.getvalue())

    def testing_display_size_x_y(self):
        sq = Square(2, 3, 2, 1)
        capturee = TestSquare_stdout.capture_stdout(sq, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capturee.getvalue())

    def testing_display_one_arg(self):
        sq = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            sq.display(1)


class TestSquare_update_args(unittest.TestCase):
    """Unittests for the testing the updated args method of the Square's class."""

    def testing_update_args_zero(self):
        sq = Square(10, 10, 10, 10)
        sq.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(sq))

    def testing_update_args_one(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(sq))

    def testing_update_args_two(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(sq))

    def testing_update_args_three(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(sq))

    def testing_update_args_four(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(sq))

    def testing_update_args_more_than_four(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(sq))

    def testing_update_args_width_setter(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2)
        self.assertEqual(2, sq.width)

    def testing_update_args_height_setter(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2)
        self.assertEqual(2, sq.height)

    def testing_update_args_None_id(self):
        sq = Square(10, 10, 10, 10)
        sq.update(None)
        correctt = "[Square] ({}) 10/10 - 10".format(sq.id)
        self.assertEqual(correctt, str(sq))

    def testing_update_args_None_id_and_more(self):
        sq = Square(10, 10, 10, 10)
        sq.update(None, 4, 5)
        correctt = "[Square] ({}) 5/10 - 4".format(sq.id)
        self.assertEqual(correctt, str(sq))

    def testing_update_args_twice(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, 3, 4)
        sq.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(sq))

    def testing_update_args_invalid_size_type(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            sq.update(89, "invalid")

    def testing_update_args_size_zero(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "width must be > 0"):
            sq.update(89, 0)

    def testing_update_args_size_negative(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "width must be > 0"):
            sq.update(89, -4)

    def testing_update_args_invalid_x(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            sq.update(89, 1, "invalid")

    def testing_update_args_x_negative(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "x must be >= 0"):
            sq.update(98, 1, -4)

    def testing_update_args_invalid_y(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            sq.update(89, 1, 2, "invalid")

    def testing_update_args_y_negative(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "y must be >= 0"):
            sq.update(98, 1, 2, -4)

    def testing_update_args_size_before_x(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            sq.update(89, "invalid", "invalid")

    def testing_update_args_size_before_y(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            sq.update(89, "invalid", 2, "invalid")

    def testing_update_args_x_before_y(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
        "x must be an integer"):
            sq.update(89, 1, "invalid", "invalid")


class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for the testing of the updated kwargs method of
    Square's class."""

    def testing_update_kwargs_one(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(sq))

    def testing_update_kwargs_two(self):
        sq = Square(10, 10, 10, 10)
        sq.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(sq))

    def testing_update_kwargs_three(self):
        sq = Square(10, 10, 10, 10)
        sq.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(sq))

    def testing_update_kwargs_four(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(sq))

    def testing_update_kwargs_width_setter(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=89, size=8)
        self.assertEqual(8, sq.width)

    def testing_update_kwargs_height_setter(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=89, size=9)
        self.assertEqual(9, sq.height)

    def testing_update_kwargs_None_id(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=None)
        correctt = "[Square] ({}) 10/10 - 10".format(sq.id)
        self.assertEqual(correctt, str(sq))

    def testing_update_kwargs_None_id_and_more(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=None, size=7, x=18)
        correctt = "[Square] ({}) 18/10 - 7".format(sq.id)
        self.assertEqual(correctt, str(sq))

    def testing_update_kwargs_twice(self):
        sq = Square(10, 10, 10, 10)
        sq.update(id=89, x=1)
        sq.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(sq))

    def testing_update_kwargs_invalid_size(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            sq.update(size="invalid")

    def testing_update_kwargs_size_zero(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "width must be > 0"):
            sq.update(size=0)

    def testing_update_kwargs_size_negative(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "width must be > 0"):
            sq.update(size=-3)

    def testing_update_kwargs_invalid_x(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            sq.update(x="invalid")

    def testing_update_kwargs_x_negative(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "x must be >= 0"):
            sq.update(x=-5)

    def testing_update_kwargs_invalid_y(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            sq.update(y="invalid")

    def testing_update_kwargs_y_negative(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "y must be >= 0"):
            sq.update(y=-5)

    def testing_update_args_and_kwargs(self):
        sq = Square(10, 10, 10, 10)
        sq.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(sq))

    def testing_update_kwargs_wrong_keys(self):
        sq = Square(10, 10, 10, 10)
        sq.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(sq))

    def testing_update_kwargs_some_wrong_keys(self):
        sq = Square(10, 10, 10, 10)
        sq.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(sq))


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for the testing of to_dictionary method of
    the Square's class."""

    def testing_to_dictionary_output(self):
        sq = Square(10, 2, 1, 1)
        correctt = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correctt, sq.to_dictionary())

    def testing_to_dictionary_no_object_changes(self):
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def testing_to_dictionary_arg(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            sq.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
