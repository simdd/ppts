from setuptools import setup, find_packages

setup(
    name='ppts',
    version='1.0.2',
    description='ppt with web',
    author='simdd',
    author_email='dev.simdd@gmail.com',
    packages=find_packages(),
    scripts=['cli/bin.py']
)
