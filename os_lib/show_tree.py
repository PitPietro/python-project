#!/usr/bin/python3.8

import os
import time


# def set_dir(path):
#     return os.chdir(path)


def show_tree(path):
    start_time = time.time()
    for root, directories, files in os.walk(path):
        base_dir = os.path.basename(os.path.normpath(path))
        print(base_dir)
        # get the current folder level as default
        level = root.replace(path, '').count(os.sep)
        # set the indent size
        indent = ' ' * 4 * level + '| '
        # print a line of the tree
        print('{}{}/'.format(indent, os.path.basename(root)))
        # double the indent
        sub_indent = ' ' * 4 * (level + 1) + '| '
        # list all the files
        for f in files:
            print('{}{}'.format(sub_indent, f))

    end_time = time.time() - start_time
    print('\nThe tree has been performed in {} seconds.'.format(end_time))


def handle_user_input():
    try:
        result = input('Insert the full path: ')
        return result
    except FileNotFoundError:
        print('ERROR: The path does not exists')


usr_input = input('Choose a path: ')
show_tree('/home/pit/Documents/script_folder/test-folder/')
