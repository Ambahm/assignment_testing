#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 14."""


# Import Python libs
import unittest

# Import student file
import escapery


class L02T14TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 14.

    """

    def test_escaped_string(self):
        """
        Tests that the string was correctly escaped.
        """
        self.assertEqual(escapery.ESCAPE_STRING, r'\n')


if __name__ == '__main__':
    unittest.main()
