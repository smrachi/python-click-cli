# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cli',
    version='0.1.0',
    description='pythonic cli using click module',
    long_description=readme,
    author='Mohsen',
    author_email='smrachi@yahoo.com',
    url='https://github.com/smrachi/python-click-cli',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

