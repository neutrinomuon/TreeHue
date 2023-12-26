from setuptools import Extension
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("version.txt","r",encoding="utf-8") as vh:
    version_description = vh.read()
    
setup( name='treehue',
       version=version_description,
       description='TreeHue is a Python package for visually enhancing directory tree structures with color-coded representations.',
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
       package_dir={"treehue": "src/python"},
       packages=['treehue'],
       data_files=[('', ['version.txt']),],
      )
    
