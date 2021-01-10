#!/usr/bin/env python3.9
from io import path
from setuptools import setup
from typing import Mapping, List



packages: List[str] = ["mrpc"]

requires: List[str] = [
    "aiohttp",
    "fastapi",
    "uvicorn",
    "orjson",
    "pyyaml",
    "pycryptodome"
]

about: Mapping[str, str] = {}




with open(path.join('', 'mrpc', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

setup(
    name=about.get['__name__'],
    version=about.get['__version__'],
    description=about.get['__description__'],
    author=about.get['__author__'],
    author_email=about.get['__email__'],
    packages=packages,
    python_requires=">=3.8",
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)
