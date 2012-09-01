# -*- coding: utf-8 -*-
# Author: Matías Bordese

from setuptools import setup, find_packages

version = '0.1'

setup(name='unrar',
      version=version,
      description="Wrapper for UnRAR library, ctypes-based.",
      keywords='unrar ctypes',
      author='Matias Bordese',
      author_email='mbordese@gmail.com',
      url='http://github.com/matiasb/python-unrar',
      license='GPL-3',
      packages=find_packages(),
     )
