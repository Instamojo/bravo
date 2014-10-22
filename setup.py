# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('bravo/bravo.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "instamojo-bravo",
    packages = ["bravo"],
    entry_points = {
        "console_scripts": ['bravo = bravo.bravo:run']
        },
    version = version,
    description = "Tool to work with HTML templates for manipulating design classes.",
    long_description = long_descr,
    author = "Instamojo Inc.",
    author_email = "dev@instamojo.com",
    url = "https://github.com/Instamojo/bravo",
    )
