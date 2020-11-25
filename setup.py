#!/usr/bin/env python3

from setuptools import setup
import setuptools

setup_dict = dict(
    name="feititfy",
    version="0.0.2a0",
    author="cjsoft",
    author_email="egwcyh@gmail.com",
    description="Notify you using feishu custom bot by webhook",
    long_description="""Notify you using feishu custom bot by webhook
    Plese refer to project homepage to get usage introduction.""",
    url="https://github.com/cjsoft/feitify",
    python_requires=">=3.5",
    packages=setuptools.find_packages(where=".", include=("feitify.*")),
    scripts=["bin/feitify"],
    install_requires=["requests"],
)
setup(**setup_dict)
