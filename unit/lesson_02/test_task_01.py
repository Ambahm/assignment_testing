#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 01."""


# Import Python libs
import unittest

# Import student file
import reassign


class L02T01TestCase(unittest.TestCase):
    """
    Test cases for lesson 02 task 01.

    """

    def test_raven(self):
        """
        Tests that the RAVEN constant value is 'Nevermore!'
        """
        self.assertEqual(reassign.RAVEN, 'Nevermore!')


if __name__ == '__main__':
    unittest.main()
