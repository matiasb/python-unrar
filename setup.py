# -*- coding: utf-8 -*-

# Copyright (C) 2012-2019  Matias Bordese
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import codecs
import os

from setuptools import find_packages, setup


# metadata
NAME = 'unrar'
DESCRIPTION = 'Wrapper for UnRAR library, ctypes-based.'
KEYWORDS = ['unrar', 'ctypes', 'rar']
URL = 'http://github.com/matiasb/python-unrar'
EMAIL = 'mbordese@gmail.com'
AUTHOR = 'Matias Bordese'
LICENSE = 'GPL-3'

HERE = os.path.abspath(os.path.dirname(__file__))

# use README as the long-description
with codecs.open(os.path.join(HERE, 'README.md'), "rb", "utf-8") as f:
    long_description = f.read()

version = __import__('unrar').__version__

setup(
    name=NAME,
    version=version,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('dependencies',)),
    license=LICENSE,
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
