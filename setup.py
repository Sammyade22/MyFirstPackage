from setuptools import setup, find_packages
setup(
    name = 'mypackage',
    version = '0.1',
    packages = find_packages(exclude = ['test*']),
    license = 'MIT',
    description = 'EDSA example python package',
    long_description = open('README.md').read(),
    install_rewuires = ['numpy'],
    url = 'https://github.com/<Sammyade22>/<package-name>',
    author = 'ADEBIYI Samuel',
    author_email = '<sammyadebiyi21@gmail.com>',
)