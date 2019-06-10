from setuptools import setup, find_packages

setup(
    name='ppts',
    version='1.0.10',
    description='ppt with web',
    author='simdd',
    author_email='dev.simdd@gmail.com',
    packages=find_packages(),
    scripts=['cli/bin.py'],
    entry_points={
        'console_scripts': [
            'ppts = cli:main',
        ]
    }
)
