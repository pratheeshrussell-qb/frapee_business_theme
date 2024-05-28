# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in whitetheme_v13/__init__.py
from business_theme import __version__ as version

setup(
	name='frapee_business_theme',
	version=version,
	description='Business theme for v13',
	author='Pratheesh',
	author_email='pratheeshrussell@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
