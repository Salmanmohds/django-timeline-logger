#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='django-timeline-logger',
    version='0.1a',
    description='Generic event logger for Django models.',
    author='Maykin Media',
    author_email='support@maykinmedia.nl',
    url='https://github.com/maykinmedia/django-timeline-logger',
    install_requires=[
        'Django>=1.8',
        'django-appconf',
    ],
    packages=find_packages(exclude=['tests*']),
    setup_requires=['pytest-runner'],
    tests_require=[
        'psycopg2',
        'pytest',
        'pytest-cov',
        'pytest-django',
        'pytest-pep8',
        'pytest-pylint',
        'pytest-pythonpath',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ]
)
