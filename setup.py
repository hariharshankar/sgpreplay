"""
"""

#!/usr/bin/env python
# vim: set sw=4 et:

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

__author__ = 'Harihar Shankar'


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_suite = True

    def run_tests(self):
        import pytest
        import sys
        import os
        cmdline = ' --cov replay -v tests/'
        errcode = pytest.main(cmdline)
        sys.exit(errcode)

setup(
    name='sgpreplay',
    version='0.0.1',
    author='Harihar Shankar',
    author_email='hariharshankar@gmail.com',
    license='',
    packages=find_packages(),
    description='Experimental replay service for signposting project',
    long_description='Experimental replay service for signposting project',
    provides=[
        'sgpreplay',
        ],
    install_requires=[
        'pywb>=0.11.4',
        ],
    dependency_links=[
    ],
    zip_safe=False,
    cmdclass={'test': PyTest},
    test_suite='',
    tests_require=[
        'pytest',
        'pytest-cov',
        'httmock',
    ])
