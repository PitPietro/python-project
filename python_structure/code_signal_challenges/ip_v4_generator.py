"""
This is not a Code Signal task: it prints all the possible IPv4 addresses
"""


def ip_v4_generator():
    for y in range(256):
        y_str = "." + str(y)
        print(y_str)


if __name__ == '__main__':
    ip_v4_generator()
