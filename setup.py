#!/usr/bin/env python

# from distutils.core import setup

# got some ideas from here: https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
#
# But apparently setuptools is the replacement for distutils, and distutils was causing problems such as
# not including the README.md file and not formatting it as Markdown on PyPI
# https://setuptools.readthedocs.io/en/latest/setuptools.html

from setuptools import setup

# import scadnano.scadnano_version as sv

# from scadnano.scadnano_version import current_version
# this is ugly, but appears to be standard practice:
# https://stackoverflow.com/questions/17583443/what-is-the-correct-way-to-share-package-version-with-setup-py-and-the-package/17626524#17626524
__version__ = open("scadnano/_version.py").readlines()[-1].split()[-1].strip("\"'")

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='scadnano_copy',
      packages=['scadnano_copy'],
      version=__version__,
      # version='0.8.0',
      download_url=f'https://github.com/UnHumbleBen/scadnano-python-package-1/archive/v{__version__}.zip',
      license='MIT',
      description="Copy for development purpose.",
      author="Benjamin Lee",
      author_email="bnllee@ucdavis.edu",
      url="https://github.com/UnHumbleBen/scadnano-python-package-1",
      long_description=long_description,
      long_description_content_type='text/markdown; variant=GFM',
      requires=['xlwt']
      )
