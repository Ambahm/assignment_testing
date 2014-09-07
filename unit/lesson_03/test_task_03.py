#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 03."""


# Import Python libs
import unittest
import mock
import random


class Lesson03Task03TestCase(unittest.TestCase):
    """
    Test cases for lesson 03 task 03.

    """

    def test_color_choices(self):
        """
        Tests that the user decision tree is followed in selecting colors.
        """
        colors = {
            'Seattle Gray': {
                'Ceramic Glaze': ['Basically White', 'White'],
                'Cumulus Nimbus': ['Off-White', 'Paper White']
            },
            'Manatee': {
                'Platinum Mist': ['Bone White', 'Just White'],
                'Spartan Sage': ['Fractal White', 'Not White']
            }
        }

        for base, accents in colors.iteritems():
            for accent, highlights in accents.iteritems():
                for highlight in highlights:
                    mock_input = [base, accent, highlight]
                    with mock.patch('__builtin__.raw_input',
                            side_effect=mock_input):
                        try:
                            task_03 = reload(task_03)
                        except NameError:
                            import task_03

                        self.assertEqual(task_03.BASE, base)
                        self.assertEqual(task_03.ACCENT, accent)
                        self.assertEqual(task_03.HIGHLIGHT, highlight)


if __name__ == '__main__':
    unittest.main()
