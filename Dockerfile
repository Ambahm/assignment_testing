# infosys-pytest-env
# 
# Version 0.2.0

FROM ubuntu:14.04
MAINTAINER Chad Heuschober "chad.heuschober@cuny.edu"

# Set locale
RUN locale-gen --no-purge en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Install python
RUN apt-get update && apt-get install -y \
    python \
    python-dev \
    python-pip \
    libxml2-dev \
    build-essential \
    libcurl3-gnutls \
    locales

# Install python libs
RUN pip install \
    pep8 \
    pylint \
    unittest2 \
    unittest-xml-reporting \
    nose \
    mockito \ 
    BeautifulSoup \
    numpy

# Setup workspaces
ENV WORKSPACE /var/workspace
