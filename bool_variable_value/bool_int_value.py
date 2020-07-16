def bool_int(name: int):
    if name:
        print('Integer value: ', name)
    else:
        print('The value is equal to 0')


if __name__ == '__main__':
    num: int = 0
    check = False

    while not check:
        try:
            num = int(input('Integer: '))
            check = True
        except ValueError:
            print(ValueError.__name__)

    bool_int(num)
