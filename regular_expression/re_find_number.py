import re

if __name__ == '__main__':
    message = 'Call 123-332-2211 from 10 am to 10pm or 667-889-4453 during the night'
    usa_phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    result = usa_phone_num_regex.findall(message)
    print(result)
