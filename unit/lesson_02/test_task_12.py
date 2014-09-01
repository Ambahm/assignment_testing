#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 12."""


# Import Python libs
import unittest

# Import student file
import semordnilap


class L02T12TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 12.

    """

    def test_napoleon_reversed(self):
        """
        Tests that the REVERSED variable exists and has the correct value.
        """
        new_value = '.ablE was I ere ,I saw elbA'

        self.assertEqual(semordnilap.REVERSED, new_value)


if __name__ == '__main__':
    unittest.main()
