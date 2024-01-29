''' This setup.py file is for installing the script of TreeHue. \
It conforms with PEP 8 guide for python'''
# --------------------------------------------------------------------
# Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
#from setuptools import Extension
from setuptools import setup

with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

with open("version.txt","r",encoding="utf-8") as vh:
    version_description = vh.read()

setup( name='TreeHue',
       version=version_description,
       description='TreeHue is a Python package for visually \
enhancing directory tree structures with color-coded representations.',
       long_description=long_description,      # Long description read from the the readme file
       long_description_content_type="text/markdown",
       author='Jean Gomes',
       author_email='antineutrinomuon@gmail.com',
       url='https://github.com/neutrinomuon/TreeHue',
       install_requires=[ 'numpy','matplotlib' ],
       classifiers=[
           "Programming Language :: Python :: 3",
           "Operating System :: OS Independent",
                   ],
       package_dir={"TreeHue": "src/python"},
       packages=['TreeHue'],
       data_files=[('', ['version.txt']),],
      )
