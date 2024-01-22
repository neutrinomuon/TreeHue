#!/usr/bin/env python3A
# -*- coding: utf-8 -*-
"""
Last version on Wed Sep 23 14:33:51 2020

RESUME : Python code for producing a tree of directory. Useful for 
distributing packages on repositories.

Version: 

@author: Jean Gomes Copyright (c)

@email: jean@astro.up.pt
    
License: TreeHue is available under the following license: LICENSE.txt in the 
distribution package.

If you would like to redistribute it  or if  you made changes please contact 
jean@astro.up.pt in order  to  avoid duplication or misuse of the package. 
This will help further imporvements and future mantainance.
"""

# import more general libraries
import os
import numpy as np

# Import necessary libraries
from pathlib import Path
from itertools import islice


# Define constants
SPACE =  '    '
BRANCH = '│   '
TEE =    '├── '
LAST =   '└── '

def inner(dir_path: Path, directories, files, prefix: str='', level=-1, **kwargs):
    #print(dir_path)

    # Access keyword arguments from the 'kwargs' dictionary
    limit_to_directories = kwargs.get('limit_to_directories', False)
    exclude_files = kwargs.get('exclude_files', '')

    if not level:
        return # 0, stop iterating
    if limit_to_directories:
        contents = [d for d in dir_path.iterdir() if d.is_dir()]
    else:
        contents = list(dir_path.iterdir())

    contents_list = np.array(contents, dtype=str)
    #print(contents_list)
    logical = False
    indices = []
    for i_ in enumerate(contents_list):
        logical_aux = False
        for k_ in exclude_files:

            l = k_ in i_[1]

            if l == True:
                logical_aux = True

        if logical_aux == True:
            logical = True
        else:
            indices.append( i_[0] )

    if logical == True and np.size(indices) > 0:
        indices = np.array(indices, dtype=int)
        contents_aux = []
        for i_ in indices:
            contents_aux.append( contents[ i_ ] )
        contents = contents_aux
        #print(contents)
        #print("logical",logical)

    pointers = [TEE] * (len(contents) - 1) + [LAST]
    for pointer, path in zip(pointers, contents):
        if path.is_dir():
            yield prefix + pointer + path.name
            directories += 1
            extension = BRANCH if pointer == TEE else SPACE
            yield from inner(path, directories, files, prefix=prefix+extension, level=level-1)
        elif not limit_to_directories:
            yield prefix + pointer + path.name
            files += 1

    return directories, files

def tree( dir_path: Path, level: int=-1, **kwargs ):
    #limit_to_directories: bool=False,
    #      length_limit: int=1000, exclude_files: str='', save_to_file: str = None ):
    """Given a directory Path object print a visual tree structure"""

    dir_path = Path(dir_path) # accept string coerceable to Path
    # Check if dir_path is '.' or './' and replace it with the current directory
    if dir_path == Path('.') or dir_path == Path('./'):
        dir_path = Path(os.getcwd())

    # Access keyword arguments from the 'kwargs' dictionary
    limit_to_directories = kwargs.get('limit_to_directories', False)
    length_limit = kwargs.get('length_limit', 1000)
    exclude_files = kwargs.get('exclude_files', '')
    save_to_file = kwargs.get('save_to_file', None)

    # Ensure save_to_file is a string
    if not isinstance(exclude_files, (str, type(None))):
        raise TypeError("exclude_files must be a string or None")

    # Ensure save_to_file is a string
    if not isinstance(save_to_file, str) and save_to_file is not None:
        raise TypeError("save_to_file must be a string or None")

    # Setting variables
    files = 0
    directories = 0

    # C0123: Use isinstance() rather than type() for a typecheck. (unidiomatic-typecheck)
    # if type(exclude_files) != list:
    #      if type(exclude_files) == str:
    #        exclude_files = [ exclude_files ]
    #    else:
    #        exclude_files = list(exclude_files)
    # Ensure exclude_files is a list
    if not isinstance(exclude_files, list):
        if isinstance(exclude_files, str):
            exclude_files = [exclude_files]
        else:
            exclude_files = list(exclude_files)

    # Print Screen
    print('#################################################')    
    print(dir_path.name)
    iterator = inner(dir_path, directories, files, level=level)
    for line in islice(iterator, length_limit):
        print(line)

    print(f'\n{directories} directories' + (f', {files} files' if files else ''))
    print('#################################################')   
    print('Generated with treehue@2024  --- © Jean Gomes ---')
    print('#################################################')

    if next(iterator, None):
        print(f'... length_limit, {length_limit}, reached, counted:')

    # print("TEST",exclude_files)
