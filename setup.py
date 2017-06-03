#!/usr/bin/env python

from setuptools import find_packages, setup


setup(
    name='oversee',
    version='1.0.0a1',
    description='Web based app to control screen contents.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Pillow==4.1.1',
        'moviepy==0.2.3.2'
    ],
    zip_safe=False,
)
