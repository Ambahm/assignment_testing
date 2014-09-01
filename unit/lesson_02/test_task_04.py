#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 02 task 04."""


# Import Python libs
import unittest

# Import student file
import artists


class L02T04TestCase(unittest.TestCase):
    """
    Tests for lesson 02 task 04.

    """

    def test_question_unchanged(self):
        """
        Tests that THE_GREAT_QUESTION value is unchanged.
        """
        question = ('Michaelangelo. Leonardo. Rafael. Donatello. Turtles? '   
                    'Creators of the great works? Both? You be the judge!')
        self.assertEqual(artists.THE_GREAT_QUESTION, question)

    def test_statements(self):
        """
        Tests the STATEMENTS value.
        """
        statements = [
                'Michaelangelo',
                'Leonardo',
                'Rafael',
                'Donatello',
                'Turtles? Creators of the great works? Both? You be the judge!'
            ]

        self.assertEqual(artists.STATEMENTS, statements)


if __name__ == '__main__':
    unittest.main()
