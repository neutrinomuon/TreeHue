#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 13:26:49 2021

@author: jean
"""

# Import general libraries
import os

# Import necessary libraries
from pathlib import Path
from itertools import islice

from datetime import datetime
from colorama import Fore, Style  # Import colorama for colored output

import numpy as np


# file_extensions_colors = {
#     '.py': Fore.RED,
#     '.pyx': Fore.BLUE,
#     '.f90': Fore.LIGHTMAGENTA_EX,
# }

SPACE = '    '
BRANCH = '│   '
TEE = '├── '
LAST = '└── '

# Get the current year
current_year = datetime.now().year

# Define a mapping of color strings to colorama color codes
color_mapping = {
    'Fore.BLACK': Fore.BLACK,
    'Fore.RED': Fore.RED,
    'Fore.GREEN': Fore.GREEN,
    'Fore.YELLOW': Fore.YELLOW,
    'Fore.BLUE': Fore.BLUE,
    'Fore.MAGENTA': Fore.MAGENTA,
    'Fore.CYAN': Fore.CYAN,
    'Fore.WHITE': Fore.WHITE,
    'Fore.LIGHTBLACK_EX': Fore.LIGHTBLACK_EX,
    'Fore.LIGHTRED_EX': Fore.LIGHTRED_EX,
    'Fore.LIGHTGREEN_EX': Fore.LIGHTGREEN_EX,
    'Fore.LIGHTYELLOW_EX': Fore.LIGHTYELLOW_EX,
    'Fore.LIGHTBLUE_EX': Fore.LIGHTBLUE_EX,
    'Fore.LIGHTMAGENTA_EX': Fore.LIGHTMAGENTA_EX,
    'Fore.LIGHTCYAN_EX': Fore.LIGHTCYAN_EX,
    'Fore.LIGHTWHITE_EX': Fore.LIGHTWHITE_EX,
}

def convert_color_string_or_keep_color(color):
    """Convert color string into a code or keep current color"""
    if isinstance(color, str):
        if color.startswith('Fore.'):
            try:
                # Look up the color code in the mapping
                color_code = color_mapping[color]
                #print(color_code)
                return color_code
            except KeyError:
                print(f"Error: Invalid color string '{color}'")
                return Fore.WHITE  # Default to white on error
        else:
            # It's already a color code string, return it as is
            return color
    else:
        return color  # If it's not a string, assume it's already a color code


def print_to_file(dir_path: Path, lines, counter, kwargs_dic):
    '''Save directory structure of your package to a file'''

    # Save structure of your package to a file in save_to_file
    if kwargs_dic['save_to_file'] is not None:
        if isinstance(kwargs_dic['save_to_file'], str):
            with open(kwargs_dic['save_to_file'], 'w', encoding='utf-8') as file:
                file.write(Fore.LIGHTRED_EX \
                           + '#################################################\n' \
                           + Style.RESET_ALL)
                file.write(Fore.RED \
                           + dir_path.name \
                           + Style.RESET_ALL \
                           + '\n')
                file.writelines([line + '\n' for line in lines])
                if counter['directories'] + counter['files'] > kwargs_dic['length_limit']:
                    file.write('... length_limit, {length_limit}, reached, counted:\n')
                file.write(Fore.YELLOW +
                           f"\n{counter['directories']} directories" +
                           (f", {counter['files']} files" if 'files' in counter else '') +
                           '\n' + Style.RESET_ALL)
                file.write(Fore.LIGHTRED_EX \
                           + '#################################################\n' \
                           + Style.RESET_ALL)
                file.write(Fore.LIGHTRED_EX \
                           + f'Generated with tree_colored @ {current_year} - © Jean Gomes\n' \
                           + Style.RESET_ALL)
                file.write(Fore.LIGHTRED_EX \
                           + '#################################################\n' \
                           + Style.RESET_ALL)


def branch_check(path: Path, characteristic, colors, kwargs_dic, contents_dic):
    '''Branch to check and set the characteristics of what will be printed'''
    # Extract components of dictionary - characteristics
    prefix = characteristic['prefix']
    pointer = characteristic['pointer']
    counter = characteristic['counter']
    color1 = characteristic['color1'] # string
    color2 = characteristic['color2'] # string

    show = characteristic['show_numbers']
    if path.is_dir():
        output = colors[color1] \
               + prefix \
               + pointer \
               + colors[color2] \
               + (str(counter['directories']) + ' ' if show else '') \
               + path.name \
               + Style.RESET_ALL
    else:
        output = colors[color1] \
               + prefix \
               + pointer \
               + colors[color2] \
               + (str(counter['files']) + ' ' if show else '') \
               + path.name \
               + Style.RESET_ALL

    # append to lines if save_to_file
    if kwargs_dic['save_to_file'] is not None:
        contents_dic['lines'].append(output)

    # Debug
    # print(characteristic['counter'])

    return output

def exclude_files_check(kwargs_dic,contents_dic):
    '''Check exclude_files if it conforms with the contents'''
    exclude_files = kwargs_dic.get('exclude_files', [])
    contents_list = contents_dic['contents_list']

    if exclude_files and exclude_files != [''] and exclude_files != '':
        if kwargs_dic['exclude_files_type'] == 'e':
            for exclude_index,exclude_element in enumerate(exclude_files):
                # Debug
                # print("Printando: ",exclude_index)
                if exclude_element[0] != '.':
                    # Debug
                    # print("EITA! Printando: ",exclude_element)
                    exclude_files[exclude_index] = '.' + exclude_element

    # print(contents_list)
    # Check if exclude_files is not empty
    if exclude_files and exclude_files != [''] and exclude_files != '':
        if kwargs_dic['exclude_files_type'] == 'e':
            filtered_contents = [Path(item) \
            for item in list(contents_list) \
                if all(Path(item).suffix != keyword for keyword in exclude_files)]
        else:
            filtered_contents = [Path(item) \
            for item in list(contents_list) \
                if all(keyword not in Path(item).name for keyword in exclude_files)]
    else:
        # If exclude_files is empty, keep all contents
        filtered_contents = [Path(item) for item in list(contents_list)]

    return filtered_contents

def inner(dir_path: Path, prefix: str = '', level=-1, **kwargs):
    '''Recursive function to check directories and files'''
    if not level:
        return # 0, stop iterating

    counter = kwargs.get('counter', {})
    kwargs_dic = kwargs.get('kwargs_dic', {})

    kwargs_dic['length_limit'] = kwargs.get('length_limit', 1000)

    # colorido= {'colors': kwargs.get('colors', {}),
    #             'file_extensions_colors': kwargs.get('file_extensions_colors', {})}

    colors = kwargs.get('colors', {})
    colors['file_extensions_colors'] = kwargs.get('file_extensions_colors', {})
    # file_extensions_colors = kwargs.get('file_extensions_colors', {})

    # Create a dictionary of contents
    contents_dic = {'contents': None,
                    'contents_list': None,
                    'pointers': None,
                    'lines': None}

    if kwargs_dic['limit_to_directories']:
        contents_dic['contents'] = [d for d in dir_path.iterdir() if d.is_dir()]
    else:
        contents_dic['contents'] = list(dir_path.iterdir())
    contents_dic['contents_list'] = np.array(contents_dic['contents'], dtype=str)

    # Call function to check exclude_files
    # Check if exclude_files to be used in filtered_contents
    # print(exclude_files)
    contents_dic['contents'] = exclude_files_check(kwargs_dic,contents_dic)
    # print(filtered_contents)

    # print(exclude_files)
    # Filter out files based on exclude_files
    # for exc in exclude_files:
    #     contents_dic['contents'] = [Path(item) \
    #                                 for item in list(contents_dic['contents_list']) \
    #                                 if all(exc not in item for exc in exc)]
    # print(contents_dic['contents'])

    # print( dir_path ) ; print( contents ) ; print( contents_list )

    contents_dic['pointers'] = [TEE] * (len(contents_dic['contents']) - 1) + [LAST]
    contents_dic['lines'] = [] if kwargs_dic['save_to_file'] is not None else None

    characteristic = {'prefix': None,
                      'pointer': None,
                      'counter': counter,
                      'show_numbers': kwargs_dic['show_numbers'],
                      'color1': 'tree_dir_color',      
                      'color2': None }

    for pointer, path in zip(contents_dic['pointers'], contents_dic['contents']):
        characteristic['prefix'] = prefix
        characteristic['pointer'] = pointer

        if path.is_dir():
            # Counter for directories
            counter['directories'] += 1

            # If the directory is a symlink
            if path.is_symlink():
                counter['directories_symlink'] += 1
                characteristic['color2'] = 'dir_symlink_color'
                yield branch_check(path, characteristic, colors, kwargs_dic, contents_dic)

                # yield colors['tree_dir_color'] \
                #     + prefix \
                #     + pointer \
                #     + colors['dir_symlink_color'] \
                #     + path.name + Style.RESET_ALL
                # # append to lines if save_to_file
                # if kwargs_dic['save_to_file'] is not None:
                #     contents_dic['lines'].append(colors['tree_dir_color'] \
                #                  + prefix + pointer \
                #                  + colors['dir_symlink_color'] \
                #                  + path.name \
                #                  + Style.RESET_ALL)

            else:
                characteristic['color2'] = 'dir_color'
                yield branch_check(path, characteristic, colors, kwargs_dic, contents_dic)

                # yield colors['tree_dir_color'] \
                #     + prefix \
                #     + pointer \
                #     + colors['dir_color'] \
                #     + path.name \
                #     + Style.RESET_ALL
                # # append to lines if save_to_file
                # if kwargs_dic['save_to_file'] is not None:
                #     contents_dic['lines'].append(colors['tree_dir_color'] \
                #                   + prefix \
                #                   + pointer \
                #                   + colors['dir_color'] \
                #                   + path.name \
                #                   + Style.RESET_ALL)

            extension = BRANCH if pointer == TEE else SPACE

            # Now, here we call inner recursively inside directory
            # Debug
            # print("Dir ----> ",path,level)
            yield from inner(path,
                             prefix=prefix + extension,
                             level=level - 1,
                             counter=counter,
                             kwargs_dic=kwargs_dic,
                             colors=colors,
                             file_extensions_colors=colors['file_extensions_colors'])
            if kwargs_dic['save_to_file'] is not None:
                # print(counter['directories'])
                # print(path)
                counter_aux = {'directories': counter['directories']-1,'files': 0}
                contents_dic['lines'].extend( inner(path,
                                    prefix=prefix + extension,
                                    level=level - 1,
                                    counter=counter_aux,
                                    kwargs_dic=kwargs_dic,
                                    colors=colors,
                                    file_extensions_colors=colors['file_extensions_colors']) )

        elif not kwargs_dic['limit_to_directories']:
            # Counter for files
            counter['files'] += 1

            file_extension =  path.suffix.lower()

            # Here are the path tp files, links...
            # Debug
            # print('----> ',path,pointer)
            # print()

            if path.is_symlink(): # Check if it's a symbolic link
                characteristic['color2'] = 'symlink_color'
                yield branch_check(path, characteristic, colors, kwargs_dic, contents_dic)
                # Counter for files
                # counter['files'] += 1

                # yield colors['tree_dir_color'] \
                #     + prefix \
                #     + pointer \
                #     + colors['symlink_color'] \
                #     + path.name \
                #     + Style.RESET_ALL
                # # append to lines if save_to_file
                # if kwargs_dic['save_to_file'] is not None:
                #     contents_dic['lines'].append(colors['tree_dir_color'] \
                #                  + prefix \
                #                  + pointer \
                #                  + colors['symlink_color'] \
                #                  + path.name \
                #                  + Style.RESET_ALL)
                counter['files_symlink'] += 1

            elif colors['file_extensions_colors'] \
                and file_extension in colors['file_extensions_colors']:
                colors['file_extension_color'] = colors['file_extensions_colors'][file_extension]
                characteristic['color2'] = 'file_extension_color'
                yield branch_check(path, characteristic, colors, kwargs_dic, contents_dic)
                # Counter for files
                # counter['files'] += 1

                # yield colors['tree_dir_color'] \
                #     + prefix \
                #     + pointer \
                #     + colors['file_extension_color'] \
                #     + path.name \
                #     + Style.RESET_ALL
                # # append to lines if save_to_file
                # if kwargs_dic['save_to_file'] is not None:
                #     contents_dic['lines'].append(colors['tree_dir_color'] \
                #                  + prefix \
                #                  + pointer \
                #                  + colors['file_extension_color'] \
                #                  + path.name \
                #                  + Style.RESET_ALL)

            else:
                characteristic['color2'] = 'file_color'
                yield branch_check(path, characteristic, colors, kwargs_dic, contents_dic)
                # Counter for files
                # counter['files'] += 1

                # yield colors['tree_dir_color'] \
                #     + prefix \
                #     + pointer \
                #     + colors['file_color'] \
                #     + path.name \
                #     + Style.RESET_ALL
                # # append to lines if save_to_file
                # if kwargs_dic['save_to_file'] is not None:
                #     contents_dic['lines'].append(colors['tree_dir_color'] \
                #                  + prefix \
                #                  + pointer \
                #                  + colors['file_color'] \
                #                  + path.name \
                #                  + Style.RESET_ALL)

        # Save structure of your package to a file in save_to_file
        print_to_file(dir_path, contents_dic['lines'], counter, kwargs_dic)

def tree(dir_path: Path,
         level: int = -1,
         colors: dict = None,
         file_extensions_colors: dict = None,
         **kwargs):
    """Given a directory Path - Print a visual tree structure"""

    dir_path = Path(dir_path)  # Accept string coerceable to Path

    # Check if dir_path is '.' or './' and replace it with the current directory
    if dir_path == Path('.') or dir_path == Path('./'):
        dir_path = Path(os.getcwd())

    # Setup a dictionary
    kwargs_dic ={ 'limit_to_directories': kwargs.get('limit_to_directories', False),
                  'length_limit': kwargs.get('length_limit', 1000),
                  'exclude_files': kwargs.get('exclude_files', ''),
                  'exclude_files_type': kwargs.get('exclude_files_type', 'e'),
                  'save_to_file': kwargs.get('save_to_file', None),
                  'show_numbers': kwargs.get('show_numbers', False)}

    # Setup a counter
    counter ={'files': 0,
              'files_symlink': 0,
              'directories': 0,
              'directories_symlink': 0}

    if not isinstance(kwargs_dic['exclude_files'], list):
        if isinstance(kwargs_dic['exclude_files'], str):
            kwargs_dic['exclude_files'] = kwargs_dic['exclude_files'].split(',')
        else:
            kwargs_dic['exclude_files'] = kwargs_dic['exclude_files']

    # Setup dictionary
    if colors is None:
        colors = {}

    colors['tree_dir_color']    = colors.get('tree_dir_color', Fore.RED)
    colors['dir_color']         = colors.get('directory', Fore.BLUE)
    colors['dir_symlink_color'] = colors.get('directory symlink', Fore.LIGHTCYAN_EX)
    colors['file_color']        = colors.get('file', Fore.GREEN)
    colors['symlink_color']     = colors.get('symlink', Fore.CYAN)
    colors['out_stats']         = colors.get('statistics', Fore.LIGHTYELLOW_EX)
    colors['out_code']          = colors.get('code', Fore.LIGHTRED_EX)

    if file_extensions_colors is not None:
        for file_extension, color_string in file_extensions_colors.items():
            file_extensions_colors[file_extension] = \
                convert_color_string_or_keep_color(color_string)

    # def inner(dir_path: Path, prefix: str = '', level=-1):
    #     nonlocal counter

    #     if not level:
    #         return # 0, stop iterating
    #     if kwargs_dic['limit_to_directories']:
    #         contents = [d for d in dir_path.iterdir() if d.is_dir()]
    #     else:
    #         contents = list(dir_path.iterdir())

    #     contents_list = np.array(contents, dtype=str)

    #     logical = False
    #     indices = []
    #     for i_index in enumerate(contents_list):
    #         logical_aux = False
    #         for k_index in kwargs_dic['exclude_files']:
    #             l_index = k_index in i_index[1]
    #             if l_index is True:
    #                 logical_aux = True
    #         if logical_aux is True:
    #             logical = True
    #         else:
    #             indices.append(i_index[0])

    #     if logical is True and np.size(indices) > 0:
    #         indices = np.array(indices, dtype=int)
    #         contents_aux = []
    #         for i_index in indices:
    #             contents_aux.append(contents[i_index])
    #         contents = contents_aux

    #     # print( dir_path ) ; print( contents ) ; print( contents_list )

    #     pointers = [TEE] * (len(contents) - 1) + [LAST]
    #     lines = [] if kwargs_dic['save_to_file'] is not None else None

    #     for pointer, path in zip(pointers, contents):
    #         if path.is_dir():
    #             if path.is_symlink():
    #                 yield colors['tree_dir_color'] \
    #                     + prefix \
    #                     + pointer \
    #                     + colors['dir_symlink_color'] \
    #                     + path.name + Style.RESET_ALL
    #                 # append to lines if save_to_file
    #                 if kwargs_dic['save_to_file'] is not None:
    #                     lines.append(colors['tree_dir_color'] \
    #                                   + prefix + pointer \
    #                                   + colors['dir_symlink_color'] \
    #                                   + path.name \
    #                                   + Style.RESET_ALL)
    #             else:
    #                 yield colors['tree_dir_color'] \
    #                     + prefix \
    #                     + pointer \
    #                     + colors['dir_color'] \
    #                     + path.name \
    #                     + Style.RESET_ALL
    #                 # append to lines if save_to_file
    #                 if kwargs_dic['save_to_file'] is not None:
    #                     lines.append(colors['tree_dir_color'] \
    #                                   + prefix \
    #                                   + pointer \
    #                                   + colors['dir_color'] \
    #                                   + path.name \
    #                                   + Style.RESET_ALL)
    #             # Counter for directories
    #             counter['directories'] += 1
    #             extension = BRANCH if pointer == TEE else SPACE
    #             yield from inner(path, prefix=prefix + extension, level=level - 1)
    #             if kwargs_dic['save_to_file'] is not None:
    #                 lines.extend(inner(path, prefix=prefix + extension, level=level - 1))
    #         elif not kwargs_dic['limit_to_directories']:
    #             file_extension =  path.suffix.lower()
    #             if path.is_symlink(): # Check if it's a symbolic link
    #                 yield colors['tree_dir_color'] \
    #                     + prefix \
    #                     + pointer \
    #                     + colors['symlink_color'] \
    #                     + path.name \
    #                     + Style.RESET_ALL
    #                 # append to lines if save_to_file
    #                 if kwargs_dic['save_to_file'] is not None:
    #                     lines.append(colors['tree_dir_color'] \
    #                                   + prefix \
    #                                   + pointer \
    #                                   + colors['symlink_color'] \
    #                                   + path.name \
    #                                   + Style.RESET_ALL)

    #             elif file_extensions_colors and file_extension in file_extensions_colors:
    #                 file_extension_color = file_extensions_colors[file_extension]
    #                 yield colors['tree_dir_color'] \
    #                     + prefix \
    #                     + pointer \
    #                     + file_extension_color \
    #                     + path.name \
    #                     + Style.RESET_ALL
    #                 # append to lines if save_to_file
    #                 if kwargs_dic['save_to_file'] is not None:
    #                     lines.append(colors['tree_dir_color'] \
    #                                   + prefix \
    #                                   + pointer \
    #                                   + file_extension_color \
    #                                   + path.name \
    #                                   + Style.RESET_ALL)

    #             # OLD tests when python file .py
    #             # elif path.suffix == '.py':
    #                 # yield colors['tree_dir_color'] \
    #                     # + prefix \
    #                     # + pointer \
    #                     # + Fore.LIGHTYELLOW_EX \
    #                     # + path.name \
    #                     # + Style.RESET_ALL
    #                 # lines.append(colors['tree_dir_color'] \
    #                               # + prefix \
    #                               # + pointer \
    #                               # + Fore.LIGHTYELLOW_EX \
    #                               # + path.name \
    #                               # + Style.RESET_ALL) \
    #                     # if save_to_file is not None else None

    #             else:
    #                 yield colors['tree_dir_color'] \
    #                     + prefix \
    #                     + pointer \
    #                     + colors['file_color'] \
    #                     + path.name \
    #                     + Style.RESET_ALL
    #                 # append to lines if save_to_file
    #                 if kwargs_dic['save_to_file'] is not None:
    #                     lines.append(colors['tree_dir_color'] \
    #                                   + prefix \
    #                                   + pointer \
    #                                   + colors['file_color'] \
    #                                   + path.name \
    #                                   + Style.RESET_ALL)
    #             # Counter for files
    #             counter['files'] += 1

    #     # Save structure of your package to a file in save_to_file
    #     if kwargs_dic['save_to_file'] is not None:
    #         if isinstance(kwargs_dic['save_to_file'], str):
    #             with open(kwargs_dic['save_to_file'], 'w', encoding='utf-8') as file:
    #                 file.write(Fore.LIGHTRED_EX \
    #                             + '#################################################\n' \
    #                             + Style.RESET_ALL)
    #                 file.write(Fore.RED \
    #                             + dir_path.name \
    #                             + Style.RESET_ALL \
    #                             + '\n')
    #                 file.writelines([line + '\n' for line in lines])
    #                 if counter['directories'] + counter['files'] > kwargs_dic['length_limit']:
    #                     file.write('... length_limit, {length_limit}, reached, counted:\n')
    #                 file.write(Fore.YELLOW +
    #                             f"\n{counter['directories']} directories" +
    #                             (f", {counter['files']} files" if 'files' in counter else '') +
    #                             '\n' + Style.RESET_ALL)
    #                 file.write(Fore.LIGHTRED_EX \
    #                             + '#################################################\n' \
    #                             + Style.RESET_ALL)
    #                 file.write(Fore.LIGHTRED_EX \
    #                   + f'Generated with tree_colored @ {current_year} - © Jean Gomes\n' \
    #                             + Style.RESET_ALL)
    #                 file.write(Fore.LIGHTRED_EX \
    #                             + '#################################################\n' \
    #                             + Style.RESET_ALL)

    # Print the directory name specified by dir_path
    print(colors['out_code'] \
          + '#################################################' \
          + Style.RESET_ALL)
    print(colors['out_code'] + dir_path.name + Style.RESET_ALL)

    # Create a single dictionary with dictionaries
    # single_dict = {'counter': counter,
    #                 'kwargs_dic': kwargs_dic,
    #                 'colors': colors,
    #                 'file_extensions_colors': file_extensions_colors}

    # prefix = ''
    iterator = inner(dir_path,
                     level=level,
                     counter=counter,
                     kwargs_dic=kwargs_dic,
                     colors=colors,
                     file_extensions_colors=file_extensions_colors)

    for line in islice(iterator, kwargs_dic['length_limit']):
        print(line)

    if next(iterator, None):
        print(f"... length_limit, {kwargs_dic['length_limit']}, reached, counted:")

    print(colors['out_stats'] \
           + f"\n{counter['directories']} directories ({counter['directories_symlink']} symlink)" \
           + (f", {counter['files']} files ({counter['files_symlink']} symlink)" \
              if 'files' in counter else '') + Style.RESET_ALL)
    print(colors['out_code']  \
          + '#################################################' \
          + Style.RESET_ALL)
    print(colors['out_code']  \
          + f'Generated: treehue_colored @{current_year} - © Jean Gomes -' \
          + Style.RESET_ALL)
    print(colors['out_code'] \
          + '#################################################' \
          + Style.RESET_ALL)
    #print("TEST", exclude_files)
