#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 13."""


# Import Python libs
import unittest

# Import student file
import semordnilap


class L02T13TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 13.

    """

    def test_reversed_titlecase(self):
        """
        Tests that the REVERSED variable exists and has the correct value.
        """
        new_value = '.Able Was I Ere ,I Saw Elba'
        self.assertEqual(semordnilap.ENTITLED, new_value)


if __name__ == '__main__':
    unittest.main()
