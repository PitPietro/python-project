message = ''
count = {}


def count_letters():
    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1

    print(count)


if __name__ == '__main__':
    message = input('Insert a world or a phrase: ')
    count_letters()
    # TODO: save the result in a SVG file (whit the commas)
