import numpy as np

data_type = {
    'type': np.int8,
    'type_code': 'xx' or ['xx', 'y'],
    'description': 'Signed/Unsigned n-bit integer type'
}

table_of_data_types = [
    # int 8-bit
    dict(data_type, type=np.int8, type_code='i1', description='Signed 8-bit integer type'),
    dict(data_type, type=np.uint8, type_code='u1', description='Unsigned 8-bit integer type'),
    # int 16-bit
    dict(data_type, type=np.int16, type_code='i2', description='Signed 16-bit integer type'),
    dict(data_type, type=np.uint16, type_code='u2', description='Unsigned 16-bit integer type'),
    # int 32-bit
    dict(data_type, type=np.int32, type_code='i4', description='Signed 32-bit integer type'),
    dict(data_type, type=np.uint32, type_code='u4', description='Unsigned 32-bit integer type'),
    # int 64-bit
    dict(data_type, type=np.int64, type_code='i8', description='Signed 64-bit integer type'),
    dict(data_type, type=np.uint64, type_code='u8', description='Unsigned 64-bit integer type'),
    # float 16-bit
    dict(data_type, type=np.float16, type_code='f2', description='Half-precision floating point'),
    # float 32-bit ~ compatible with C programming language
    dict(data_type, type=np.float32, type_code=['f4', 'f'], description='Standard single-precision floating point'),
    # float 64-bit
    dict(data_type, type=np.float64, type_code=['f8', 'd'], description='Standard double-precision floating point'),
    # float 128-bit
    dict(data_type, type=np.float128, type_code=['f16', 'g'], description='Extended-precision floating point'),
    # complex 64-bit
    dict(data_type, type=np.complex64, type_code='c8', description='Complex number made up by two 32-bit floats'),
    # complex 128-bit
    dict(data_type, type=np.complex128, type_code='c16', description='Complex number made up by two 64-bit floats'),
    # complex 256-bit
    dict(data_type, type=np.complex256, type_code='c32', description='Complex number made up by two 128-bit floats'),
    # other types
    dict(data_type, type=np.bool, type_code='?', description='Boolean type'),
    dict(data_type, type=np.object, type_code='O', description='Python object type'),
    # 1 byte per char
    dict(data_type, type=np.string_, type_code='S', description='Fixed-length ASCII string type'),
    # n° of bytes is platform specific
    dict(data_type, type=np.unicode_, type_code='U', description='Fixed-length Unicode type'),
]

if __name__ == '__main__':
    for data_type in table_of_data_types:
        print(data_type)

# first = {'x': 1, 'y': 100, 'foo': 'bar'}
# second = dict(first, x=2, y=200)  # {'y': 200, 'x': 2, 'foo': 'bar'}
# https://docs.python.org/3/library/stdtypes.html#dict
