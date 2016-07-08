#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
requirements = [pkg.split('=')[0] for pkg in open('requirements.txt').readlines()]

description = "Commandline tool to send free SMS via http://www.meet.net.np"

long_description = open("README.rst").read()

classifiers = ['Environment :: Console',
               'Programming Language :: Python :: 3'
               ]

version = open('CHANGES.txt').readlines()[0][1:].strip()

setup(name='ntc-websms',
      version=version,
      description=description,
      author='Sandip Bhagat',
      author_email='sandipbgt@gmail.com',
      url='https://github.com/sandipbgt/ntc-websms',
      scripts=['src/meet',],
      install_requires=requirements,
      long_description=long_description,
      packages=['ntc_websms'],
      package_dir = {'ntc_websms': 'src/ntc_websms'},
      classifiers=classifiers
    )