#!/usr/bin/env python

from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='har2jmeter',
    version='0.1',
    description='Tool to convert har (Http ARchive) files to jMeter load tests',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/dmonego/har2jmeter',
    install_requires=['jinja2>=2.7.3'],
    scripts=["har2jmeter.py"],
    packages=['har2jmeter_utils'],
    package_data={'har2jmeter_utils': ['templates/*']},
    keywords=['jmeter', 'http archive', 'har2jmx', 'command line', 'cli']
)
