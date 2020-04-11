"""
This is not a Code Signal task: it prints all the possible IPv4 addresses
"""


def ip_v4_generator():
    range_n = 256
    iterator = 0
    for k in range(range_n):
        iterator += 1
        k_str = "." + str(k)
        for y in range(range_n):
            iterator += 1
            y_str = "." + str(y)
            result = k_str + y_str
            print("{}\tn° {}".format(result, iterator))


if __name__ == '__main__':
    ip_v4_generator()
