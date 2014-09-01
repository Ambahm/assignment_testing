#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 17."""


# Import Python libs
import unittest

# Import student file
import simple_types


class L02T17TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 17.

    """

    def test_is_true(self):
        """
        Tests that the IS_TRUE variable exists and has the correct value.
        """
        self.assertTrue(simple_types.IS_TRUE)

    def test_is_false(self):
        """
        Tests that the IS_FALSE variable exists and has the correct value.
        """
        self.assertFalse(simple_types.IS_FALSE)

    def test_is_none(self):
        """
        Tests that the IS_NONE variable exists and has the correct value.
        """
        self.assertIsNone(simple_types.IS_NONE)

    def test_integer_equivs(self):
        """
        Tests that the INTEGER_EQUIVS variable exists and has the correct
        value.
        """
        self.assertTrue(simple_types.INTEGER_EQUIVS)


if __name__ == '__main__':
    unittest.main()
