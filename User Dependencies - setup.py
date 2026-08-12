# User Dependencies 

from setuptools import setup, find_packages

# Add install requirements
setup(
    author="<your-name>",
    description="A package for converting imperial lengths and weights.",
    name="impyrial",
    packages=find_packages(include=["impyrial", "impyrial.*"]),
    version="0.1.0",
    install_requires=['numpy>=1.10', 'pandas'],
)
# the install requirement was added to on line 12 we defined the install_requires parameters to add dependencies.
# If any version of a package is acceptable, then you can simply add 'package' to the install_requires list.
