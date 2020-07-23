#!/usr/bin/python3.8

import os

'''
This script calculate the total size of a folder given its absolute path.
'''


def get_total_size_folder(full_path='/'):
    total_size = 0
    for filename in os.listdir(full_path):
        file_path = os.path.join(full_path, filename)
        if not os.path.isfile(file_path):
            continue
        total_size += os.path.getsize(file_path)
    return total_size


def handle_user_input():
    try:
        result = input('Insert the full path: ')
        return result
    except FileNotFoundError:
        print('ERROR: The path does not exists')


usr_input = handle_user_input()
print(get_total_size_folder(usr_input))


'''
RUN the script:
$ cd os_lib
$ chmod 774 calc_total_size_folder.py (only one time)
$ ./calc_total_size_folder.py
'''