#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 03."""


# Import Python libs
import unittest
import mock
import random

# Import user libs
import task_03


class Lesson03Task03TestCase(unittest.TestCase):
    """
    Test cases for lesson 03 task 03.

    """

    def test_color_choices(self):
        """
        Tests that the user decision tree is followed in selecting colors.
        """
        colors = {
            'seattle gray': {
                'ceramic glaze': ['basically white', 'white'],
                'cumulus nimbus': ['off-white', 'paper white']
            },
            'manatee': {
                'platinum mist': ['bone white', 'just white'],
                'spartan sage': ['fractal white', 'not white']
            }
        }

        for base, accents in colors.iteritems():
            for accent, highlights in accents.iteritems():
                for highlight in highlights:
                    mock_input = [base, accent, highlight]
                    with mock.patch('__builtin__.raw_input',
                            side_effect=mock_input):
                        task_03 = reload(task_03)

                        self.assertEqual(task_03.BASE.lower(), base)
                        self.assertEqual(task_03.ACCENT.lower(), accent)
                        self.assertEqual(task_03.HIGHLIGHT.lower(), highlight)


if __name__ == '__main__':
    unittest.main()
