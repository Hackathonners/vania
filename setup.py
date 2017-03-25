# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="vania",
    version="0.1.0",
    description="A module to fairly distribute tasks considering people preferences.",
    license="MIT",
    author="Hackathonners",
    packages=find_packages(),
    install_requires=[
        'pulp',
    ],
    package_dir={'': 'src'},
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
