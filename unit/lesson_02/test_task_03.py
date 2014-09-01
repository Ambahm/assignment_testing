#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 03."""


# Import Python libs
import unittest

# Import student file
import lost_in_space


class L02T03TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 03.

    """

    def test_klaxon(self):
        """
        Tests that the KLAXON value is correct
        """
        klaxon = 'Danger ' * 5
        self.assertEqual(lost_in_space.KLAXON, klaxon)


if __name__ == '__main__':
    unittest.main()
