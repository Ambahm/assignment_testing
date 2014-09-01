#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 06."""


# Import Python libs
import unittest

# Import student file
import artists


class L02T06TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 06.

    """

    def test_num_artists(self):
        """
        Tests the NUM_ARTISTS value.
        """
        self.assertIs(artists.NUM_ARTISTS, 4)

    def test_num_characters(self):
        """
        Tests the CHARACTERS value.
        """
        self.assertIs(artists.CHARACTERS, 105)


if __name__ == '__main__':
    unittest.main()
