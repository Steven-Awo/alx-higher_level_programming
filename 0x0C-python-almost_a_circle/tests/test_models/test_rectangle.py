#!/usr/bin/python3

"""Defining the unittests for the models/rectangle.py.

Unittest classes:
    TestRectangle_instantiation - line 24
    TestRectangle_width - line 115
    TestRectangle_height - line 193
    TestRectangle_x - line 264
    TestRectangle_y - line 336
    TestRectangle_order_of_initialization - line 404
    TestRectangle_area - line 434
    TestRectangle_update_args - line 541
    TestRectangle_update_kwargs - line 679
    TestRectangle_to_dictionary - line 792
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for the testing the instantiation of the
    Rectangle's class."""

    def testing_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def testing_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def testing_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def testing_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def testing_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def testing_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def testing_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def testing_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def testing_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def testing_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def testing_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def testing_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def testing_width_getter(self):
        rc = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rc.width)

    def testing_width_setter(self):
        rc = Rectangle(5, 7, 7, 5, 1)
        rc.width = 10
        self.assertEqual(10, rc.width)

    def testing_height_getter(self):
        rc = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rc.height)

    def testing_height_setter(self):
        rc = Rectangle(5, 7, 7, 5, 1)
        rc.height = 10
        self.assertEqual(10, rc.height)

    def testing_x_getter(self):
        rc = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rc.x)

    def testing_x_setter(self):
        rc = Rectangle(5, 7, 7, 5, 1)
        rc.x = 10
        self.assertEqual(10, rc.x)

    def testing_y_getter(self):
        rc = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rc.y)

    def testing_y_setter(self):
        rc = Rectangle(5, 7, 7, 5, 1)
        rc.y = 10
        self.assertEqual(10, rc.y)


class TestRectangle_width(unittest.TestCase):
    """Unittests for the testing the initialization of the
    Rectangle width attribute."""

    def testing_None_width(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle(None, 2)

    def testing_str_width(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle("invalid", 2)

    def testing_float_width(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle(5.5, 1)

    def testing_complex_width(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle(complex(5), 2)

    def testing_dict_width(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def testing_bool_width(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle(True, 2)

    def testing_list_width(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def testing_set_width(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def testing_tuple_width(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def testing_frozenset_width(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 1}), 2)

    def testing_range_width(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle(range(5), 2)

    def testing_bytes_width(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle(b'Python', 2)

    def testing_bytearray_width(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 2)

    def testing_memoryview_width(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle(memoryview(b'abcedfg'), 2)

    def testing_inf_width(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle(float('inf'), 2)

    def testing_nan_width(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle(float('nan'), 2)

    def testing_negative_width(self):
        with self.assertRaisesRegex(ValueError,
                "width must be > 0"):
            Rectangle(-1, 2)

    def testing_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectangle_height(unittest.TestCase):
    """Unittests for the testing of the initialization of the
    Rectangle's height attribute."""

    def testing_None_height(self):
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            Rectangle(1, None)

    def testing_str_height(self):
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            Rectangle(1, "invalid")

    def testing_float_height(self):
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            Rectangle(1, 5.5)

    def testing_complex_height(self):
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            Rectangle(1, complex(5))

    def testing_dict_height(self):
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})

    def testing_list_height(self):
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def testing_set_height(self):
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def testing_tuple_height(self):
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def testing_frozenset_height(self):
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3, 1}))

    def testing_range_height(self):
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            Rectangle(1, range(5))

    def testing_bytes_height(self):
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            Rectangle(1, b'Python')

    def testing_bytearray_height(self):
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            Rectangle(1, bytearray(b'abcdefg'))

    def testing_memoryview_height(self):
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            Rectangle(1, memoryview(b'abcedfg'))

    def testing_inf_height(self):
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            Rectangle(1, float('inf'))

    def testing_nan_height(self):
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            Rectangle(1, float('nan'))

    def testing_negative_height(self):
        with self.assertRaisesRegex(ValueError,
                "height must be > 0"):
            Rectangle(1, -1)

    def testing_zero_height(self):
        with self.assertRaisesRegex(ValueError,
                "height must be > 0"):
            Rectangle(1, 0)


class TestRectangle_x(unittest.TestCase):
    """Unittests for the testing the initialization of the
    Rectangle's x attribute."""

    def testing_None_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Rectangle(1, 2, None)

    def testing_str_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def testing_float_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def testing_complex_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def testing_dict_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def testing_bool_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Rectangle(1, 2, True, 2)

    def testing_list_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def testing_set_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def testing_tuple_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def testing_frozenset_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def testing_range_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Rectangle(1, 2, range(5))

    def testing_bytes_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Rectangle(1, 2, b'Python')

    def testing_bytearray_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def testing_memoryview_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Rectangle(1, 2, memoryview(b'abcedfg'))

    def testing_inf_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Rectangle(1, 2, float('inf'), 2)

    def testing_nan_x(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Rectangle(1, 2, float('nan'), 2)

    def testing_negative_x(self):
        with self.assertRaisesRegex(ValueError,
                "x must be >= 0"):
            Rectangle(5, 3, -1, 0)


class TestRectangle_y(unittest.TestCase):
    """Unittests for the testing the initialization of the
    Rectangle's y attribute."""

    def testing_None_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def testing_str_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def testing_float_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def testing_complex_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def testing_dict_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def testing_list_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def testing_set_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def testing_tuple_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def testing_frozenset_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def testing_range_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def testing_bytes_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Rectangle(1, 2, 3, b'Python')

    def testing_bytearray_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def testing_memoryview_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))

    def testing_inf_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Rectangle(1, 2, 1, float('inf'))

    def testing_nan_y(self):
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def testing_negative_y(self):
        with self.assertRaisesRegex(ValueError,
                "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectangle_order_of_initialization(unittest.TestCase):
    """Unittests for the testing the Rectangle order of the
    attribute's initialization."""

    def testing_width_before_height(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def testing_width_before_x(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def testing_width_before_y(self):
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def testing_height_before_x(self):
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def testing_height_before_y(self):
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def testing_x_before_y(self):
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangle_area(unittest.TestCase):
    """Unittests for the testing the the area method of
    the Rectangle's class."""

    def testing_area_small(self):
        rc = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, rc.area())

    def testing_area_large(self):
        rc = Rectangle(999999999999999,
                999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, rc.area())

    def testing_area_changed_attributes(self):
        rc = Rectangle(2, 10, 1, 1, 1)
        rc.width = 7
        rc.height = 14
        self.assertEqual(98, rc.area())

    def testing_area_one_arg(self):
        rc = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            rc.area(1)


class TestRectangle_stdout(unittest.TestCase):
    """Unittests for the testing the __str__ and the display methods of the
    Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Capturing and returning the text printed to the stdout.

        Args:
            rect (Rectangle): The Rectangle to be printed to the stdout.
            method (str): The method used to run on the rect.
        Returns:
            The text to be printed to the stdout by calling the method on sq.
        """
        capturee = io.StringIO()
        sys.stdout = capturee
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capturee

    def testing_str_method_print_width_height(self):
        rc = Rectangle(4, 6)
        capturee = TestRectangle_stdout.capture_stdout(rc, "print")
        correctt = "[Rectangle] ({}) 0/0 - 4/6\n".format(rc.id)
        self.assertEqual(correctt, capturee.getvalue())

    def testing_str_method_width_height_x(self):
        rc = Rectangle(5, 5, 1)
        correctt = "[Rectangle] ({}) 1/0 - 5/5".format(rc.id)
        self.assertEqual(correctt, rc.__str__())

    def testing_str_method_width_height_x_y(self):
        rc = Rectangle(1, 8, 2, 4)
        correctt = "[Rectangle] ({}) 2/4 - 1/8".format(rc.id)
        self.assertEqual(correctt, str(rc))

    def testing_str_method_width_height_x_y_id(self):
        rc = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(rc))

    def testing_str_method_changed_attributes(self):
        rc = Rectangle(7, 7, 0, 0, [4])
        rc.width = 15
        rc.height = 1
        rc.x = 8
        rc.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(rc))

    def testing_str_method_one_arg(self):
        rc = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rc.__str__(1)

    def testing_display_width_height(self):
        rc = Rectangle(2, 3, 0, 0, 0)
        capturee = TestRectangle_stdout.capture_stdout(rc,
                "display")
        self.assertEqual("##\n##\n##\n", capturee.getvalue())

    def testing_display_width_height_x(self):
        rc = Rectangle(3, 2, 1, 0, 1)
        capturee = TestRectangle_stdout.capture_stdout(rc,
                "display")
        self.assertEqual(" ###\n ###\n", capturee.getvalue())

    def testing_display_width_height_y(self):
        rc = Rectangle(4, 5, 0, 1, 0)
        capturee = TestRectangle_stdout.capture_stdout(rc,
                "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capturee.getvalue())

    def testing_display_width_height_x_y(self):
        rc = Rectangle(2, 4, 3, 2, 0)
        capturee = TestRectangle_stdout.capture_stdout(rc,
                "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capturee.getvalue())

    def testing_display_one_arg(self):
        rc = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            rc.display(1)


class TestRectangle_update_args(unittest.TestCase):
    """Unittests for the testing the update args method of
    the Rectangle's class."""

    def testing_update_args_zero(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rc))

    def testing_update_args_one(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(rc))

    def testing_update_args_two(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rc))

    def testing_update_args_three(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rc))

    def testing_update_args_four(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(rc))

    def testing_update_args_five(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rc))

    def testing_update_args_more_than_five(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rc))

    def testing_update_args_None_id(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(None)
        correctt = "[Rectangle] ({}) 10/10 - 10/10".format(rc.id)
        self.assertEqual(correctt, str(rc))

    def testing_update_args_None_id_and_more(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(None, 4, 5, 2)
        correctt = "[Rectangle] ({}) 2/10 - 4/5".format(rc.id)
        self.assertEqual(correctt, str(rc))

    def testing_update_args_twice(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(89, 2, 3, 4, 5, 6)
        rc.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(rc))

    def testing_update_args_invalid_width_type(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            rc.update(89, "invalid")

    def testing_update_args_width_zero(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "width must be > 0"):
            rc.update(89, 0)

    def testing_update_args_width_negative(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "width must be > 0"):
            rc.update(89, -5)

    def testing_update_args_invalid_height_type(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            rc.update(89, 2, "invalid")

    def testing_update_args_height_zero(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "height must be > 0"):
            rc.update(89, 1, 0)

    def testing_update_args_height_negative(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "height must be > 0"):
            rc.update(89, 1, -5)

    def testing_update_args_invalid_x_type(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            rc.update(89, 2, 3, "invalid")

    def testing_update_args_x_negative(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "x must be >= 0"):
            rc.update(89, 1, 2, -6)

    def testing_update_args_invalid_y(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            rc.update(89, 2, 3, 4, "invalid")

    def testing_update_args_y_negative(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "y must be >= 0"):
            rc.update(89, 1, 2, 3, -6)

    def testing_update_args_width_before_height(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            rc.update(89, "invalid", "invalid")

    def testing_update_args_width_before_x(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            rc.update(89, "invalid", 1, "invalid")

    def testing_update_args_width_before_y(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            rc.update(89, "invalid", 1, 2, "invalid")

    def testing_update_args_height_before_x(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            rc.update(89, 1, "invalid", "invalid")

    def testing_update_args_height_before_y(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            rc.update(89, 1, "invalid", 1, "invalid")

    def testing_update_args_x_before_y(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            rc.update(89, 1, 2, "invalid", "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for the testing the update kwargs method of the
    Rectangle's class."""

    def testing_update_kwargs_one(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(rc))

    def testing_update_kwargs_two(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(rc))

    def testing_update_kwargs_three(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rc))

    def testing_update_kwargs_four(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(rc))

    def testing_update_kwargs_five(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(rc))

    def testing_update_kwargs_None_id(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(id=None)
        correctt = "[Rectangle] ({}) 10/10 - 10/10".format(rc.id)
        self.assertEqual(correctt, str(rc))

    def testing_update_kwargs_None_id_and_more(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(id=None, height=7, y=9)
        correctt = "[Rectangle] ({}) 10/9 - 10/7".format(rc.id)
        self.assertEqual(correctt, str(rc))

    def testing_update_kwargs_twice(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(id=89, x=1, height=2)
        rc.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(rc))

    def testing_update_kwargs_invalid_width_type(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "width must be an integer"):
            rc.update(width="invalid")

    def testing_update_kwargs_width_zero(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "width must be > 0"):
            rc.update(width=0)

    def testing_update_kwargs_width_negative(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "width must be > 0"):
            rc.update(width=-5)

    def testing_update_kwargs_invalid_height_type(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "height must be an integer"):
            rc.update(height="invalid")

    def testing_update_kwargs_height_zero(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "height must be > 0"):
            rc.update(height=0)

    def testing_update_kwargs_height_negative(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "height must be > 0"):
            rc.update(height=-5)

    def testing_update_kwargs_inavlid_x_type(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "x must be an integer"):
            rc.update(x="invalid")

    def testing_update_kwargs_x_negative(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "x must be >= 0"):
            rc.update(x=-5)

    def testing_update_kwargs_invalid_y_type(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError,
                "y must be an integer"):
            rc.update(y="invalid")

    def testing_update_kwargs_y_negative(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError,
                "y must be >= 0"):
            rc.update(y=-5)

    def testing_update_args_and_kwargs(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rc))

    def testing_update_kwargs_wrong_keys(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rc))

    def testing_update_kwargs_some_wrong_keys(self):
        rc = Rectangle(10, 10, 10, 10, 10)
        rc.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(rc))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for the testing the to_dictionary method of the
    Rectangle's class."""

    def testing_to_dictionary_output(self):
        rc = Rectangle(10, 2, 1, 9, 5)
        correctt = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correctt, rc.to_dictionary())

    def testing_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def testing_to_dictionary_arg(self):
        rc = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            rc.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
