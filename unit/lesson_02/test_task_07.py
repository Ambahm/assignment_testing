#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 07."""


# Import Python libs
import unittest

# Import student file
import artists


class L02T07TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 07.

    """

    def test_has_creators(self):
        """
        Tests the HAS_CREATORS value.
        """
        self.assertTrue(artists.HAS_CREATORS)

    def test_has_splinter(self):
        """
        Tests the HAS_SPLINTER value.
        """
        self.assertFalse(artists.HAS_SPLINTER)


if __name__ == '__main__':
    unittest.main()
