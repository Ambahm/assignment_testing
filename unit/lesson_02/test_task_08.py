#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 08."""


# Import Python libs
import unittest

# Import student file
import stripped


class L02T08TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 08.

    """

    def test_nervous_as(self):
        """
        Tests that the NERVOUS_AS value has been stripped.
        """
        newval = 'A long-tailed cat in a room full of rockin\' chairs.'
        self.assertEqual(stripped.NERVOUS_AS, newval)


if __name__ == '__main__':
    unittest.main()
