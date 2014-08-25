#!/bin/sh

SRCROOT="${WORKSPACE}/src"
TESTROOT="${WORKSPACE}/testing"
LOGDIR="${TESTROOT}/target"

# might need to change this to sr
export PYTHONPATH="${PYTHONPATH}:${TESTROOT}:${SRCROOT}"

# lint tests
pylint --rcfile="${TESTROOT}/pylintrc" "${SRCROOT}" | tee "${LOGDIR}/pylint.log"

# unit tests
nosetests -w "${TESTROOT}/unit/${LESSON_ID}" --with-xunit --xunit-file="${LOGDIR}/nosetest.xml"

