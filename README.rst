IS 210: Software Application Programming
****************************************

Welcome to IS 210: Software Application Programming

.. contents:: Table of Contents

Repository Cloning
==================

[stub]

Tests (Optional)
========================

Code and syntax checks may be optionally run on-site by the following methods.
These are the same tests that will be executed upon a pull request.

PyLint
------

Linting is a form of syntax checking that enforces conformance to best practices
in code writing and documentation. While it is generally best to strive for 100%
success in linting, there are instances where the lint checker may cause
spurious warnings or errors. If you believe you have received a spurious
notification, please wait for your instructor to assist you. They will be able
to identify unnecessary warnings.

To execute linting for all lesson packages, please type the following from the
testing root:

    .. code-block:: bash

        PYTHONPATH=$PYTHONPATH$PWD$SRCDIR pylint -r n $SRCDIR

Where ``$SRCDIR`` is the location of the source code to be linted

Unittest
--------

Unit tests are discrete tests that seek to test the smallest possible unit of
code in an application. Such tests are usually written to test the functionality
of a single function or parameter and are bundled together in TestCases. The
benefit of unit tests is their ability to be run quickly and guarantee that
methods and modules have predictable input and output.

This course will use unit tests extensively in order to test that student
work conforms to the expected input/output standards at a minimum.

To execute unit tests, type the following from the project root:

    .. code-block:: bash

        PYTHONPATH=$PYTHONPATH:$SRCDIR nosetests -w unit/$LESSON_ID

Where ``$SRCDIR`` is the test-able code source and ``$LESSON_ID`` is the test
lesson folder id.

Continuous Integration
----------------------

    .. code-block:: bash

        git clone git@github.com:cheuschober/jenkins-docker-executors.git
        cd jenkins-docker-executors
        docker build -t jenkins-docker .
        docker run --name jenkins-docker -i -t -v /var/run/docker.sock:/var/run/docker.sock -p 8080:8080 -e "JENKINS_HOME=/var/jenkins_home" -v /my/persistent/store:/var/jenkins_home jenkins-docker


The above will set up a useable docker server, however, if you wish to run the tests yourself,
use the following commands.

    .. code-block:: bash

        mkdir workspace
        cd workspace
        git clone git@github.com:is210-faculty/assignment_proto.git src
        git clone git@github.com:is210-faculty/assignment_testing.git testing

        cd testing
        docker build -t infosys-pytest-env .
        docker run --rm -e WORKSPACE=/var/workspace -e LESSON_ID=$LESSON_ID -v ../:/var/workspace infosys-pytest-env /var/workspace/testing/build.sh

Where ``$LESSON_ID`` is the UD of the lesson whose tests will be run.
