#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 02."""


# Import Python libs
import unittest
import mock
import random

# Import user libs
import task_02


class Lesson03Task02TestCase(unittest.TestCase):
    """
    Test cases for lesson 03 task 02.

    """

    def test_blood_pressure_status(self):
        """
        Tests that the correct ``BP_STATUS`` is returned.'
        """
        levels = {'low': [-256, 90],
                  'ideal': [90, 119],
                  'warning': [120, 139],
                  'high': [140, 160],
                  'emergency': [160, 256]
        }

        for key, value in levels.iteritems():
            systolic = random.randint(value[0], value[1])
            with mock.patch('__builtin__.raw_input',  return_value=systolic):
                task_02 = reload(task_02)
                self.assertEqual(task_02.BP_STATUS.lower(), key)


if __name__ == '__main__':
    unittest.main()
