#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 18."""


# Import Python libs
import unittest

# Import student file
import conversion


class L02T18TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 18.

    """

    def test_thanks_for_the_fish(self):
        """
        Tests that the THANKS_FOR_THE_FISH variable exists and has the correct
        value.
        """
        thanks = 'The answer to life, the universe, and everything? It\'s 42'
        self.assertEqual(conversion.THANKS_FOR_THE_FISH, thanks)


if __name__ == '__main__':
    unittest.main()
