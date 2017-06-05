#!/usr/bin/env python
# -*- coding: utf-8 -*-


from yeecli import __version__
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    "yeelight>=0.3.0",
    "click>=6.6",
]

test_requirements = [
]

setup(
    name='yeecli',
    version=__version__,
    description="yeecli is a command-line utility for controlling the YeeLight RGB LED lightbulb.",
    long_description=readme,
    author="Stavros Korokithakis",
    author_email='hi@stavros.io',
    url='https://github.com/skorokithakis/yeecli',
    packages=[
        'yeecli',
    ],
    package_dir={'yeecli':
                 'yeecli'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords="yeelight xiaomi led rgb yeecli",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        'console_scripts': [
            'yeecli=yeecli.cli:cli',
            'yee=yeecli.cli:cli',
        ],
    },
)
