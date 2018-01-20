#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='requestsapp',
    version='0.0.1',
    description='An app that does lots of requests',
    author='JvMaiia',
    author_email='joaovmferreira@gmail.com',
    license='BSD license',
    packages=find_packages(
        exclude=['docs', 'tests', 'android']
    ),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: BSD license',
    ],
    install_requires=[
    ],
    options={
        'app': {
            'formal_name': 'Request App',
            'bundle': 'com.example'
        },
    }
)
