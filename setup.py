# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Automagit',
    version='0.1.0',
    description='A hungry bot looking for differences between followers in my github profile, day by day',
    long_description=readme,
    author='Lorenzo Pieri',
    author_email='-',
    url='https://github.com/404answernotfound/automagit',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

