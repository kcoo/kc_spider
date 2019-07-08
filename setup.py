#!/usr/bin/python
# coding: utf-8

from setuptools import setup, find_packages

setup(
    name="kc_spider",
    version="0.0.1",
    license='Private',
    author='yangchao',
    author_email='yc.fqiyou@gmail.com',
    url='https://github.com/kcoo/kc_spider',
    description="scan-tools",
    packages=find_packages(),
    package_dir={'': '.'},
    install_requires=[

    ],
    entry_points="""
    [console_scripts]
    scan_github = foo.github.scan:main
    """,
)
