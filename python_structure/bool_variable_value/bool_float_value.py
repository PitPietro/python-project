def bool_float(name: float):
    if name:
        print('Float value: ', name)
    else:
        print('The value is equal to 0.0')


if __name__ == '__main__':
    num: float = 0.0
    check = False

    while not check:
        try:
            num = float(input('Float: '))
            check = True
        except ValueError:
            print(ValueError.__name__)

    bool_float(num)
