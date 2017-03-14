#!/usr/bin/env python

import sys
from setuptools import setup

requires = []

# if sys.version_info[0] == 2:
#     requires += ['python-dateutil>=1.0, != 2.0']
# else
#     ['python-dateutil >= 2.0']

setup(
    name='semiconductor',
    version='0.0.1',
    description='Async HTTP Server for parallelism and concurrency.',
    author='Gustavo Cavalcante',
    author_email='me@guscavalcante.com',
    url='https://github.com/thatgustavo/semiconductor',
    packages=['semiconductor'],
    install_requires=requires,
    include_package_data=True,
    license='',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
)
