#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="push",
    version=0.1,
    description='push plus script', 
    
    author='bbat',
    author_email = "amoblin@ossxp.com",
    url="",
    packages=find_packages(),
    platforms = "Independant",
    
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: BSD',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    # Choose your license
    license='MIT',
    py_modules=['push'],
    zip_safe=False,
    include_package_data=True,
)