#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 04."""


# Import Python libs
import unittest
import mock
import random

# Import user libs
import task_04


class Lesson03Task04TestCase(unittest.TestCase):
    """
    Test cases for lesson 03 task 04.

    """

    def test_weekend(self):
        """
        Tests that it will snooze for a weekend after 0600, eg 'Sunday'.
        """
            mock_input['Sunday', '0700']
            with mock.patch('__builtin__.raw_input', side_effect=mock_input):
                task_04 = reload(task_04)
                self.assertTrue(task_04.SNOOZE)

    def test_weekend_abbr(self):
        """
        Tests that it will snooze for a weekend abbreviation, eg 'Sun'.
        """
            mock_input['Sun', '0700']
            with mock.patch('__builtin__.raw_input', side_effect=mock_input):
                task_04 = reload(task_04)
                self.assertTrue(task_04.SNOOZE)


    def test_weekend_casing(self):
        """
        Tests that it will snooze for a weekend with unusual casing.
        """
            mock_input['sUnDay', '0700']
            with mock.patch('__builtin__.raw_input', side_effect=mock_input):
                task_04 = reload(task_04)
                self.assertTrue(task_04.SNOOZE)


    def test_weekday_snooze(self):
        """
        Tests that it will snooze for a weekday at '0500'.
        """
            mock_input['Monday', '0500']
            with mock.patch('__builtin__.raw_input', side_effect=mock_input):
                task_04 = reload(task_04)
                self.assertTrue(task_04.SNOOZE)


    def test_weekday_late_snooze(self):
        """
        Tests that it will not snooze for a weekday at '2300'.
        """
            mock_input['Monday', '2300']
            with mock.patch('__builtin__.raw_input', side_effect=mock_input):
                task_04 = reload(task_04)
                self.assertFalse(task_04.SNOOZE)


if __name__ == '__main__':
    unittest.main()
