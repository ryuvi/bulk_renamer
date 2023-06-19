#!/usr/bin/env python

from distutils.core import setup
from re import search

setup(name='bulk_renamer',
      version='1.0',
      description='Software to rename multiple files',
      author=['ryuvi', 'HPereiraVitor'],
      author_email=['vicenters10@gmail.com'],
      url='',
      packages=[search(r'\w+(?=\=)', package).group() for package in open('requirements.txt', 'r').readlines()],
      package_dir={'bulk_renamer': 'lib'}
     )