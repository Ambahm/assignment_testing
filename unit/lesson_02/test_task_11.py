#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 11."""


# Import Python libs
import unittest

# Import student file
import flemish


class L02T11TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 11.

    """

    def test_flemish(self):
        """
        Tests that the FLEMISH variable exists and has the correct value.
        """
        post_replace = expectation.FISHY.replace('Spanish', 'Flemish', 1)
        self.assertEqual(expectation.FLEMISH, post_replace)


if __name__ == '__main__':
    unittest.main()
