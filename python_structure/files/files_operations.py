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
        my_file.write("Hi Python!")


def file_read():
    """
    It's possible to call read() on a file once, each time it is opened.
    Save the file contents in a variable or container to use it later in the program.
    :return:
    """
    with open("p.txt", "r") as my_file:
        content = my_file.read()
    print(content)


if __name__ == '__main__':
    file_open()
    file_read()
