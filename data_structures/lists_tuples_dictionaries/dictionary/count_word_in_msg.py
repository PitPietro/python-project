import pprint

message = ''
count = {}


def count_letters():
    for character in message.lower():
        count.setdefault(character, 0)
        count[character] = count[character] + 1

    final_dict = pprint.pformat(count)
    print(final_dict)


if __name__ == '__main__':
    message = input('Insert a world or a phrase: ')
    count_letters()
    # TODO: save the result in a SVG file (whit the commas)
    # TODO: replace the input whit the reading of a .txt file
    #  (it allows the study of the frequency for a specific cryptography method)
    # TODO: Make a cake diagram from it and display it whit pandas!
