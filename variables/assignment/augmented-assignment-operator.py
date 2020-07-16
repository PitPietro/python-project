def plus_n(var: int, n: int):
    var += n
    return var


def less_n(var: int, n: int):
    var -= n
    return var


def for_n(var: int, n: int):
    var *= n
    return var


def divided_n(var: int, n: int):
    var /= n
    return var


def modulo_n(var: int, n: int):
    var %= n
    return var


if __name__ == '__main__':
    a = 20
    b = 3
    msg = '{} {} {} = {}'
    print(msg.format(a, '+', b, plus_n(a, b)))
    print(msg.format(a, '-', b, less_n(a, b)))
    print(msg.format(a, '*', b, for_n(a, b)))
    print(msg.format(a, '/', b, divided_n(a, b)))
    print(msg.format(a, '%', b, modulo_n(a, b)))
