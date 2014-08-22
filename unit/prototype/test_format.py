# -*- coding: utf-8 -*-

#!/usr/bin/env python

# Import Python libs
import unittest


# Import user libs
import format


class FormatTestCase(unittest.TestCase):
    '''
    Tests if the student successfully formatted a constant.
    '''


    def test_string_format(self):
        '''
        Tests if MYSTRING has the correct value.
        '''
        val = '24 is the number of months I have on my contract.\n It, ' \
            '24, is also the name of my sister\'s favorite TV show.'
        self.assertEqual(format.MYSTRING, val)


if __name__ == '__main__':
    unittest.main()
        
