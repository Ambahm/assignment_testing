#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 09."""


# Import Python libs
import unittest

# Import student file
import inquisition


class L02T09TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 09.

    """

    def test_module_docstring_length(self):
        """
        Tests that the module has a docstring at least 3 lines long.
        """
        numlines = len(inquisition.__doc__.splitlines())
        self.assertGreaterEqual(numlines, 3)


if __name__ == '__main__':
    unittest.main()
