#!/bin/sh

SRCROOT="${WORKSPACE}/src"
TESTROOT="${WORKSPACE}/testing"
LOGDIR="${TESTROOT}/target"

# might need to change this to sr
export PYTHONPATH="${PYTHONPATH}:${TESTROOT}:${SRCROOT}"

# lint tests
find "${SRCROOT}" -type f -iname "*.py" -print0 | while read -d $'\0' file
do
    pylint --rcfile="${TESTROOT}/pylintrc" "${file}" | tee -a "${LOGDIR}/pylint.log"
done

# unit tests
nosetests -w "${TESTROOT}/unit/${LESSON_ID}" --with-xunit --xunit-file="${LOGDIR}/nosetest.xml"

