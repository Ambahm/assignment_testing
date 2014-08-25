#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson_01."""

# Import Python libs
import hashlib
import unittest
from . import stdcapture

with stdcapture.StdCapture() as hello_output:
    import hello_world

class HelloWorldTestCase(unittest.TestCase):
    """
    Test cases for lesson_01, hello_world.

    Attributes:
        hello_output (string): String output from importing ``hello_world``

    """

    def test_hello_world(self):
        """
        Tests that 'Hello World!' has been changed to include username.
        """
        regex = r'Hello (?!World)(\w|-)+!'
        self.assertRegexpMatches(hello_output[0], regex)

    def test_jenkins_access(self):
        """
        Test that always fails but returns a commit code.
        """
        hello_sha256 = hashlib.sha256('Hello World!').hexdigest()
        output_sha256 = hashlib.sha256(hello_output[0]).hexdigest()

        if hello_sha256 != output_sha256:
            msg = 'Good Job! This test is EXPECTED to fail. Your code is: {0}'
            msg = msg.format(output_sha256)
        else:
            msg = (
                'You must change the output of ``hello_world`` before you can '
                'receive your commit code.'
            )

        self.fail(msg=msg)


if __name__ == '__main__':
    unittest.main()
