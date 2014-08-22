# -*- coding: utf-8 -*-

#!/usr/bin/env python

# Import Python libs
import unittest

# Import user libs
try:
    import integer
    import_success = True
except ImportError:
    import_success = False


class IntegerTestCase(unittest.TestCase):
    '''
    Tests if the student successfully created the integer file.
    '''


    def test_import_success(self):
        '''
        Tests whether or not the student successfully created the file
        '''
        self.assertTrue(import_success, msg='Could not import integer file')


    def test_cars_value(self):
        '''
        Tests if the variable was created and has a value.
        '''
        self.assertTrue(hasattr(integer, 'cars'),
                        msg='The cars variable is missing from this file.')
        self.assertEqual(integer.cars, 100)


if __name__ == '__main__':
    unittest.main()
        
