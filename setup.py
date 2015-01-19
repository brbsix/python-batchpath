# -*- coding: utf-8 -*-

from setuptools import setup
from batchpath import __version__


def read(filename):
    with open(filename) as fd:
        return fd.read()


setup(
    name='batchpath',
    version=__version__,
    author='Brian Beffa',
    author_email='brbsix@gmail.com',
    description="Utilities to generate and verify pathnames",
    long_description=read('README.rst'),
    url='https://github.com/brbsix/python-batchpath',
    license='GPLv2',
    keywords='os.walk, pathnames, paths',
    py_modules=['batchpath'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development',
        'Topic :: System :: Filesystems',
    ],
)
