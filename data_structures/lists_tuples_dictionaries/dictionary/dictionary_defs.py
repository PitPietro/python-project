"""
Dictionary key must be immutable
"""
string_dict = dict({"1": "1st", "2": "2nd", "3": "3rd"})


def add_element_to_string_dict(key: str, value: str):
    string_dict[key] = value


def delete_element_to_string_dict(key: str):
    del string_dict[key]


def get_element_from_string_dict(key: str):
    if key in string_dict:
        print("key: {} \t value: {}".format(key, string_dict[key]))
    else:
        print("key {} not found".format(key))


def are_equal(dict_one, dict_two):
    return dict_one == dict_two


def is_key_in_dict(key, my_dict):
    return key in my_dict


def list_keys(my_dict):
    return list(my_dict.keys())


def list_values(my_dict):
    return list(my_dict.values())


def list_items(my_dict):
    return list(my_dict.items())


def print_info(my_dict):
    for k in my_dict.keys():
        print('\t', k)

    print('')
    for v in my_dict.values():
        print('\t', v)

    print('')
    for k, v in my_dict.items():
        print('\t', k, v)


def set_default(my_dict, key, value):
    my_dict.setdefault(key, value)
    return my_dict


if __name__ == '__main__':
    print('base dict\n', string_dict)
    add_element_to_string_dict("4", "4rd")
    print('add an element\n', string_dict)
    delete_element_to_string_dict("2")
    print('delete an element\n', string_dict)
    get_element_from_string_dict("8")
    print('getting an element\n', string_dict)
    get_element_from_string_dict("4")

    a = {'name': 'Pit', 'age': 423}
    b = {'age': 423, 'name': 'Pit'}
    print('compare two dicts\n', are_equal(a, b))
    print('look for a key in a dict\n', is_key_in_dict('hello', a))

    print('list all the keys of a dict\n', list_keys(string_dict))
    print('list all the values of a dict\n', list_values(string_dict))
    print('list all the items of a dict\n', list_items(string_dict))
    print('\nInfo: \n')
    print_info(string_dict)
    print('Set a new key whit its value\n', set_default(string_dict, '5', '5th'))
