#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 05."""


# Import Python libs
import unittest

# Import student file
import artists


class L02T05TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 05.

    """

    def test_artists(self):
        """
        Tests the ARTISTS value.
        """
        turtles = [
                'Michaelangelo',
                'Leonardo',
                'Rafael',
                'Donatello',
            ]

        self.assertEqual(artists.ARTISTS, turtles)


if __name__ == '__main__':
    unittest.main()
