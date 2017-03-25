# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import setuptools.command.build_py
import subprocess


class GenDocsCommand(setuptools.command.build_py.build_py):

    """Command to generate docs."""

    def run(self):
        subprocess.Popen(
            ['pdoc', '--html', 'vania/', '--html-dir=docs', '--overwrite'])
        setuptools.command.build_py.build_py.run(self)

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="vania",
    version="0.1.1",
    description="A module to fairly distribute objects among targets considering weights.",
    license="MIT",
    author="Hackathonners",
    author_email="contact@hackathonners.org",
    packages=find_packages(),
    install_requires=[
        'pulp',
        'pdoc'
    ],
    package_dir={'': '.'},
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    cmdclass={
        'gendocs': GenDocsCommand
    },
)
