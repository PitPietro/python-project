#!/usr/bin/python3.8

import os


# def set_dir(path):
#     return os.chdir(path)


def show_tree(path):
    for folder_name, sub_folders, file_names in os.walk(path):
        print('folder: ', folder_name)
        print('Sub-folders in {} are {}'.format(folder_name, str(sub_folders)))
        print('Files in {} are {}'.format(folder_name, str(file_names)))


def handle_user_input():
    try:
        result = input('Insert the full path: ')
        return result
    except FileNotFoundError:
        print('ERROR: The path does not exists')


usr_input = input('Choose a path: ')
show_tree(usr_input)
