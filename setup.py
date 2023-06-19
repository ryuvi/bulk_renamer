#!/usr/bin/env python

from distutils.core import setup

setup(name='bulk_renamer',
      version='1.0',
      description='Software to rename multiple files',
      author=['ryuvi', 'HPereiraVitor'],
      author_email=['vicenters10@gmail.com'],
      url='',
      packages=['black', 'tk'],
      package_dir={'bulk_renamer': 'lib'}
     )