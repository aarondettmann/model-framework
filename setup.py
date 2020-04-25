#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools
import os

from src.mframework.__version__ import __version__

NAME = 'model-framework'
VERSION = __version__
AUTHOR = 'Aaron Dettmann'
EMAIL = 'dettmann@kth.se'
DESCRIPTION = ''
URL = 'Framework to build consistent model interfaces '
REQUIRES_PYTHON = '>=3.6.0'
REQUIRED = []
README = 'README.rst'
PACKAGE_DIR = 'src/'
LICENSE = 'Apache License 2.0'


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, README), "r") as fp:
    long_description = fp.read()

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    url=URL,
    include_package_data=True,
    package_dir={'': PACKAGE_DIR},
    license=LICENSE,
    packages=[NAME],
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    # See: https://pypi.org/classifiers/
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
    ],
)
