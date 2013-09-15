#!/usr/bin/env python
from setuptools import setup

import release

setup(
    author=release.author,
    author_email=release.author_email,
    name=release.name,
    version=release.version,
    install_requires=[
        'EvyWorker',
    ],
    entry_points={
        'evy.extensions': [
            'email = extension:Email',
        ]
    }
)
