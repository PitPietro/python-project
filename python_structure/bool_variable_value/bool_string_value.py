def bool_string(name):
    if name:
        print('String value: ', name)
    else:
        print('Please insert a world')


if __name__ == '__main__':
    bool_string(input('String: '))
