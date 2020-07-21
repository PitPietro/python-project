import re


def find_usa_phone():
    message = 'Call 123-332-2211 from 10 am to 10pm or 667-889-4453 during the night'
    usa_phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    result = usa_phone_num_regex.findall(message)
    return result


def find_usa_phone_with_groups():
    message = 'My number is 123-332-2211'
    # (area code)-(number)
    # (\d\d\d)-(\d\d\d-\d\d\d\d)
    usa_phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    result = usa_phone_num_regex.search(message)
    my_list = [
        result.group(),
        result.group(1),
        result.group(2)
    ]
    return my_list


def eu_prefix_number():
    msg = 'Call me at (+39) 111 00 44 230'
    # \( means we're looking for a parenthesis, it is not the start of a group
    phone_regex = re.compile(r'\(\+\d\d\)\s\d\d\d \d\d \d\d \d\d\d')
    result = phone_regex.search(msg)
    print(result.group())


def optional_eu_prefix_number():
    msg = 'Call me at (+51) 111 00 44 230'
    phone_regex = re.compile(r'(\(\+\d\d\)\s)?\d\d\d \d\d \d\d \d\d\d')
    result = phone_regex.search(msg)
    print(result.group())


if __name__ == '__main__':
    print(find_usa_phone())
    num_list = find_usa_phone_with_groups()
    print('{} --> area group: {} -- number: {}'.format(num_list[0], num_list[1], num_list[2]))
    eu_prefix_number()
    optional_eu_prefix_number()
