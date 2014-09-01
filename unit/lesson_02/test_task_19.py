#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 19."""


# Import Python libs
import unittest

# Import student file
import formatted


class L02T19TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 19.

    """

    def test_email(self):
        """
        Tests that the EMAIL variable exists and has the correct value.
        """
        email = ('Hi Pat! I have *amazing* news! I won the raffle with '
                 'number 000042!')
        self.assertEqual(formatted.EMAIL, email)

    def test_formatting_string(self):
        """
        Tests that the NEWS variable was modified properly.

        If modified correctly, other values should be possible.
        """
        email_tc = ('Hi Alex! I have drab news! I won the raffle with '
                 'number 005678!')
        email_fmt = formatted.NEWS.format('drab', 5678, friend='Alex')
        self.assertEqual(email_fmt, email_tc)
        



if __name__ == '__main__':
    unittest.main()
