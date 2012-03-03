#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="django-liveserver",
    version="0.1a-2",
    packages=[
        'django_liveserver',
    ],

    install_requires=['django>=1.3'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst', '*.md'],
    },

    # metadata for upload to PyPI
    author="Alec Koumjian",
    author_email="akoumjian@gmail.com",
    description="A backport of the Django 1.4 LiveServerTestCase for 1.3",
    keywords="django live server selenium test testcase",
    long_description=open('README.md').read()
)
