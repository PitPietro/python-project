"""
This is not a Code Signal task: it prints all the possible IPv4 addresses
"""
import time


def ip_v4_generator():
    range_n = 256
    iterator = 0
    for i in range(range_n):
        iterator += 1
        i_str = str(i)
        for j in range(range_n):
            iterator += 1
            j_str = "." + str(j)
            for k in range(range_n):
                iterator += 1
                k_str = "." + str(k)
                for y in range(range_n):
                    iterator += 1
                    y_str = "." + str(y)
                    result = i_str + j_str + k_str + y_str
                    print("{}\tn° {}".format(result, iterator))


if __name__ == '__main__':
    start_i = time.clock()
    ip_v4_generator()
    end_i = time.clock()
    print("time: {} seconds".format(end_i - start_i))
