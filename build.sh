#!/bin/sh

SRCROOT="src"
TESTROOT="testing"
LOGDIR="${TESTROOT}/target"

# might need to change this to sr
export PYTHONPATH="${PYTHONPATH}:${WORKSPACE}/${TESTROOT}:${WORKSPACE}/${SRCROOT}"

# get started in the right location
cd "${WORKSPACE}"

# lint tests
find "${SRCROOT}" -type f -iname "*.py" -print0 | while read -d $'\0' file
do
    pylint --rcfile="${TESTROOT}/pylintrc" "${file}" | tee -a "${LOGDIR}/pylint.log"
done

# unit tests
nosetests -w "${TESTROOT}/unit/${LESSON_ID}" --with-xunit --xunit-file="${LOGDIR}/nosetest.xml"

