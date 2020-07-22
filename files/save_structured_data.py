import shelve

LIST_FILE_NAME = 'my_list.pd'


def write_list():
    shelf_file = shelve.open(LIST_FILE_NAME)
    shelf_file['languages'] = ['C', 'Go', 'Java', 'Javascript', 'PHP', 'Python', 'Ruby', 'Perl']
    shelf_file.close()


def read_list(index):
    shelf_file = shelve.open(LIST_FILE_NAME)
    return shelf_file[index]


def read_list_keys():
    shelf_file = shelve.open(LIST_FILE_NAME)
    return list(shelf_file.keys())


if __name__ == '__main__':
    print('Write the content of a file . . .')
    write_list()
    print('Read the content of a file:\n')
    print(read_list('languages'))
    print('my_list keys: ', read_list_keys())
    exit(0)
