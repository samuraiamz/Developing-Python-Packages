# The final step before you can install your package impyrial is to write the setup.py file.

# In this exercise, you'll write this file, including all the metadata for your package.

# P.S. If you look into the impyrial source code, you'll see a new subpackage has been added to convert weights.

# Import required functions - Import the setup() and find_packages() functions from setuptools.
from setuptools import setup, find_packages

# Call setup function - Fill out the metadata, including your name.
# Give it the version number 0.1.0 and the description "A package for converting impyrial lengths and weights."
# Use the find_packages() function to include the package and its subpackages.
setup(
    author="<your-name>",
    description="A package for converting imperial lengths and weights.",
    name="impyrial",
    packages=find_packages(include=["impyrial", "impyrial.*"]),
    version="0.1.0",
)
