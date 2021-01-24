#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name="prelude-protobuf",
    version="1.0.0",
    author="Marc PEREZ",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=['protobuf']
)
