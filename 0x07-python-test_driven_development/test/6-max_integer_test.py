#!/usr/bin/python3
"""Unittestses for the max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defining the unittests for the max_integer([..])."""

    def test_ordered_list(self):
        """Testing an ordered list of only integers."""
        orderedd = [1, 2, 3, 4]
        self.assertEqual(max_integer(orderedd), 4)

    def test_unordered_list(self):
        """Testing an unorderedd list of only integers."""
        unorderedd = [1, 2, 4, 3]
        self.assertEqual(max_integer(unorderedd), 4)

    def test_max_at_begginning(self):
        """Testing a list with the beginning a max value."""
        max_at_begin = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_begin), 4)

    def test_empty_list(self):
        """Testing for an emptyy list."""
        emptyy = []
        self.assertEqual(max_integer(emptyy), None)

    def test_one_element_list(self):
        """Testing a list with only a single element."""
        one_elmnt = [7]
        self.assertEqual(max_integer(one_elmnt), 7)

    def test_floats(self):
        """Testing a list of only floatss."""
        floatss = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floatss), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floatss."""
        ints_nd_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_nd_floats), 15.5)

    def test_string(self):
        """Testing a strg."""
        strg = "Brennan"
        self.assertEqual(max_integer(strg), 'r')

    def test_list_of_strings(self):
        """Testing a list of only strgs."""
        strgs = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strgs), "name")

    def test_empty_string(self):
        """Testing an emptyy strg."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
