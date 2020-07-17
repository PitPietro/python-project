def is_usa_phone_number(msg):
    if len(msg) != 12:
        return False
    for i in range(0, 3):
        if not msg[i].isdecimal():
            return False
    if msg[3] != '-':
        return False
    for i in range(4, 7):
        if not msg[i].isdecimal():
            return False
    if msg[7] != '-':
        return False
    for i in range(8, 12):
        if not msg[i].isdecimal():
            return False
    return True


def search_usa_phone_number(msg):
    found_num = False
    for i in range(len(msg)):
        chunk = msg[i: i+12]
        if is_usa_phone_number(chunk):
            print('USA phone number found: ', chunk)
            found_num = True
    if not found_num:
        print('No USA phone number found')


if __name__ == '__main__':
    message = 'Call 123-332-2211 from 10 am to 10pm or 667-889-4453 during the night'
    search_usa_phone_number(message)
