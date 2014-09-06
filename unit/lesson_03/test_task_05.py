#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 03 task 05."""


# Import Python libs
import unittest
import mock
import random
import decimal
import sys

# Import user libs
import task_04


class Lesson03Task05TestCase(unittest.TestCase):
    """
    Test cases for lesson 03 task 05.

    """

    def __init__(self):
        super(Lesson03Task05TestCase, self).__init__()
        self.test_data = [
                [0, 199999, 1, 15, True, '3.63'],
                [0, 199999, 1, 15, False, '4.65'],
                [0, 199999, 16, 20, True, '4.04'],
                [0, 199999, 16, 20, False, '4.98'],
                [0, 199999, 21, 30, True, '5.77'],
                [0, 199999, 21, 30, False, '6.39'],
                [200000, 999999, 1, 15, True, '3.02'],
                [200000, 999999, 1, 15, False, '3.98'],
                [200000, 999999, 16, 20, True, '3.27'],
                [200000, 999999, 16, 20, False, '4.08'],
                [200000, 999999, 21, 30, True, '4.66'],
                [1000000, sys.maxint, 1, 15, True, '2.05'],
                [1000000, sys.maxint, 16, 20, True, '2.62'],
                [-200000, -100000, 1, 15, True, None],
                [200000, 999999, 21, 30, False, None],
                [1000000, sys.maxint, 1, 15, False, None],
                [1000000, sys.maxint, 21, 30, True, None],
                [0, 199999, 31, 40, True, None],
        ]

    def calculate_interest(self, principal, rate, yrs):
        """
        Calculates a total for interest + principal when compounded monthly.
        """
        if rate:
            dec_rt = decimal.Decimal(rate)
            total = int(round(principal * ((1 + (dec_rt / 12)) ** (12 * yrs)))
        else:
            total = None

        return total


    def get_bool_value(self, strval):
        return True if strval[0:1].lower() == 'y' else False

    def test_total(self):
        """
        Tests for the value of ``TOTAL``.
        """
        for data in self.test_data:
            principal = random.randint(data[0], data[1])
            years = random.randint(data[2], data[3])
            total = self.calculate_interest(principal, data[5], years)

            mock_input['Mountebank Singes', principal, years, data[4]]
            with mock.patch('__builtin__.raw_input', side_effect=mock_input):
                task_05 = reload(task_05)
                self.assertEqual(total, task_05.TOTAL)

if __name__ == '__main__':
    unittest.main()
