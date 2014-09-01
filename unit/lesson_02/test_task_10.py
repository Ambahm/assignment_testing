#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 10."""


# Import Python libs
import re
import unittest

# Import student file
import expectation


class L02T10TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 10.

    """

    def test_fishy(self):
        """
        Tests that the FISHY variable exists and has the correct value.
        """
        regex = re.compile('surprise')
        post_replace = regex.sub('haddock', expectation.inquisition.SPANISH)
        self.assertEqual(expectation.FISHY, post_replace)


if __name__ == '__main__':
    unittest.main()
