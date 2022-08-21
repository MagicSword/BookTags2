# -*- coding: utf-8 -*-

# Learn more: https://github.com/MagicSword/BookTags2

from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="booktags2",
    version="0.1.0",
    description="BookTags2",
    long_description=readme,
    author="MagicSword",
    author_email="magicsword@gmail.com",
    url="https://github.com/MagicSword/BookTags2",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
