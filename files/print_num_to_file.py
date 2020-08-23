def print_numbers(max_n):
    msg = ''
    for i in range(max_n + 1):
        msg += str(i) + '\n'
        # print('msg: {}|i: {}'.format(msg, i))
    return msg


def write_file(content):
    print(content)
    file = open('numbers.txt', 'w')
    file.write(content)
    file.close()


if __name__ == '__main__':
    write_file(print_numbers(100))
