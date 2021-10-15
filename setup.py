from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'Convert binary, hex, octal, decimal'
LONG_DESCRIPTION = 'A package that allows to convert num number  (binary, hex, octal, decimal)'

# Setting up
setup(
    name="mathconvert",
    version=VERSION,
    author="Ayoub Ech-chetyouy",
    author_email="<ayoubechchetyouy@yahoo.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'math', 'convert', 'binary', 'hex', 'octal', 'To', 'decimal'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
