#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 15."""


# Import Python libs
import unittest
from decimal import Decimal
from fractions import Fraction

# Import student file
import numtypes


class L02T15TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 15.

    """

    def test_floatvar(self):
        """
        Tests that the FLOATVAR variable exists and has the correct value.
        """
        self.assertEqual(numtypes.FLOATVAR, 0.1)

    def test_decimalvar(self):
        """
        Tests that the DECIMALVAR variable exists and has the correct value.
        """
        self.assertEqual(numtypes.DECIMALVAR, Decimal('0.1'))

    def test_fractionvar(self):
        """
        Tests that the FRACTIONVAR variable exists and has the correct value.
        """
        self.assertEqual(numtypes.FRACTIONVAR, Fraction(1, 10))


if __name__ == '__main__':
    unittest.main()
