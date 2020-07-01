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


if __name__ == '__main__':
    print(string_dict)
    add_element_to_string_dict("4", "4rd")
    print(string_dict)
    delete_element_to_string_dict("2")
    print(string_dict)
    get_element_from_string_dict("8")
    print(string_dict)
    get_element_from_string_dict("4")