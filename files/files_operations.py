def file_open():
    """
    A file can be opened in three modes:
    - r: read only
    - w: write only
    - w+: read and write

    open([file_path], [mode])
    A 'with' statement performs an action automatically when Python finishes executing it.

    :return:
    """
    with open("p.txt", "w+") as my_file:
        msg = input('Insert the file content: ')
        my_file.write(msg)


def file_read():
    """
    It's possible to call read() on a file once, each time it is opened.
    Save the file contents in a variable or container to use it later in the program.
    :return:
    """
    with open("p.txt", "r") as my_file:
        content = my_file.read()
    return content


def read_file_by_line():
    with open('p.txt', 'r') as my_file:
        text_lines = my_file.readlines()
    return text_lines


if __name__ == '__main__':
    print('Open a file and write something inside:\n')
    file_open()
    print('Read the content of that file:\n')
    print(file_read())
    print('|-------------------')
    print(read_file_by_line())
    exit(0)
