#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 16."""


# Import Python libs
import unittest

# Import student file
import numtypes


class L02T16TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 16.

    """

    def test_df_equality(self):
        """
        Tests that the DF_EQUALITY variable exists and has the correct value.
        """
        self.assertFalse(numtypes.DF_EQUALITY)

    def test_are_inequal(self):
        """
        Tests that the ARE_INEQUAL variable exists and has the correct value.
        """
        self.assertTrue(numtypes.ARE_INEQUAL)


if __name__ == '__main__':
    unittest.main()
