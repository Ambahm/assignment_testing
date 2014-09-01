#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 20."""


# Import Python libs
import unittest

# Import student file
import identity


class L02T20TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 20.

    """

    def test_empty_string(self):
        """
        Tests that ``is_empty()`` returns True when passed an empty string.
        """
        self.assertTrue(identity.is_empty(''))

    def test_nonempty_string(self):
        """
        Tests that ``is_empty()`` returns False when passed a non-empty string.
        """
        self.assertFalse(identity.is_empty('Ni'))

    def test_nonsequence_exception(self):
        """
        Tests that ``is_empty()`` raises an exception when not passed a
        sequence object-type.
        """
        with self.assertRaises(TypeError):
            identity.is_empty(None)
        

if __name__ == '__main__':
    unittest.main()
