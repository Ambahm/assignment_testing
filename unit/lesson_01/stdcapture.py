#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides StdCapture class."""

# Import Python libs
import sys
from cStringIO import StringIO

class StdCapture(list):
    """Simple list lass for capturing stdout.

    Examples:

        Capture one print statement.
        >>> with StdCapture() as output:
        >>>     print 'Hello World'
        >>>
        >>>
        >>> print output
        ['Hello World']

        Capture chain-load it for multiple calls.
        >>> with StdCapture() as output:
        >>>     print 'Hello World'
        >>>
        >>>
        >>> with StdCapture(output) as output:
        >>>     print 'Hello Shirley'
        >>>
        >>>
        >>> print output
        ['Hello World', 'Hello Shirley']

    """

    def __enter__(self):
        """
        Starts stdout and stringio capture.

            Returns:
                self, An instance of this object.

        """
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        """
        Parses stringio capture and returns stdout back to sys.

        """
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout
