#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 01."""


# Import Python libs
import unittest
import mock
import random

class Lesson03Task01TestCase(unittest.TestCase):
    """
    Test cases for lesson 03 task 01.

    """

    def test_raw_input(self):
        """
        Tests that the input values are stored into the correct variables.'
        """
        values = ['The Ministry of Funny Walks', random.randint(-999, 999)]
        with mock.patch('__builtin__.raw_input',  side_effect=values):
            import task_01
            self.assertEqual(task_01.QUESTION_01, values[0])
            self.assertEqual(task_01.QUESTION_02, values[1])


if __name__ == '__main__':
    unittest.main()
