#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = ["rpy2>=3.4.5", "numpy", "scipy", "pandas"]

test_requirements = [ ]

setup(
    author="T. Moudiki",
    author_email='thierry.moudiki@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Diffusion models for finance, insurance, economics, physics",
    install_requires=requirements,
    license="BSD Clause Clear license",
    long_description="Python port of R package 'esgtoolkit' (https://techtonique.github.io/esgtoolkit/)",
    include_package_data=True,
    keywords='esgtoolkit',
    name='esgtoolkit',
    packages=find_packages(include=['esgtoolkit', 'esgtoolkit.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Techtonique/esgtoolkit_python',
    version='1.0.0',
    zip_safe=False,
)
