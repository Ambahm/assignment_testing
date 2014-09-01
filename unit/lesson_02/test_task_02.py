#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 02."""


# Import Python libs
import unittest

# Import student file
import integer_math


class L02T02TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 02.

    """

    def test_weeks(self):
        """
        Tests that the WEEKS constant value is 52
        """
        self.assertIs(integer_math.WEEKS, 52)


if __name__ == '__main__':
    unittest.main()
