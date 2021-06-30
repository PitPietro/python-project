import numpy as np

data_type = {
    'type': np.int8,
    'type_code': 'xx',
    'description': 'Signed/Unsigned n-bit integer type'
}

table_of_data_types = [
    # 8-bit
    dict(data_type, type=np.int8, type_code='i1', description='Signed 8-bit integer type'),
    dict(data_type, type=np.uint8, type_code='u1', description='Unsigned 8-bit integer type'),
    # 16-bit
    dict(data_type, type=np.int16, type_code='i2', description='Signed 16-bit integer type'),
    dict(data_type, type=np.uint16, type_code='u2', description='Unsigned 16-bit integer type')
]

if __name__ == '__main__':
    for data_type in table_of_data_types:
        print(data_type)

# first = {'x': 1, 'y': 100, 'foo': 'bar'}
# second = dict(first, x=2, y=200)  # {'y': 200, 'x': 2, 'foo': 'bar'}
# https://docs.python.org/3/library/stdtypes.html#dict
