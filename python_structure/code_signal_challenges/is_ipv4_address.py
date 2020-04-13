"""
> Task
An IP address is a numerical label assigned to each device (e.g., computer, printer)
participating in a computer network that uses the Internet Protocol for communication.
There are two versions of the Internet protocol, and thus two versions of addresses.
One of them is the IPv4 address. Given a string, find out if it satisfies the
IPv4 address naming rules.

> Example
For ip = "172.16.254.1", the output should be true;
For ip = "172.316.254.1", the output should be false.
316 is not in range [0, 255].
For ip = ".254.255.0", the output should be false.
There is no first number.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: string ip
A string consisting of digits, full stops and lowercase English letters.
- guaranteed constraints:
1 ≤ inputString.length ≤ 30.
- output: boolean
true if inputString satisfies the IPv4 address naming rules, false otherwise.
"""
from python_structure.code_signal_challenges.result_is_correct import is_correct
import time
import ipaddress


def is_ipv4_address(ip):
    """
    step 1: find the dots' indexes
    step 2: check if the strings between the dots are digit
    :param ip:
    :return:
    """
    if not 7 <= len(ip) <= 15:
        print("\tlength: {}".format(len(ip)))
        return False
    indexes = []
    for i in range(len(ip)):
        if ip[i] == ".":
            indexes.append(i)
    if len(indexes) != 3:
        return False
    num_1 = is_number(ip, 0, indexes[0])
    num_2 = is_number(ip, indexes[0] + 1, indexes[1])
    num_3 = is_number(ip, indexes[1] + 1, indexes[2])
    num_4 = is_number(ip, indexes[2] + 1, len(ip))
    print(num_1)
    print(num_2)
    print(num_3)
    print(num_4)
    if num_1 == -1 or num_2 == -1 or num_3 == -1 or num_4 == -1:
        return False
    else:
        return True


def is_number(ip_add, start_i, end_i):
    num = ""
    for j in range(start_i, end_i):
        digit = ip_add[j]
        if digit.isdigit():
            num += ip_add[j]
        else:
            return -1
    if num == "" or num == "00" or num == "000" or int(num) > 255:
        return -1
    if num.startswith("0") and len(num) > 1:
        return -1
    else:
        return num


def double_for_range():
    """
    print 3 ranges
    :return: None
    """
    r = [0, 4, 8]
    for i in range(len(r)):
        for j in range(4):
            index = j + r[i]
            print(index)
        print("_")


def is_ipv4_address_built_in(ip_v4):
    try:
        ipaddress.ip_address(ip_v4)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    # double_for_range()
    print("Pit-made function:")
    start_pit = time.clock()
    is_correct(is_ipv4_address("172.16.254.1"), True)
    is_correct(is_ipv4_address("172.316.254.1"), False)
    is_correct(is_ipv4_address(".254.255.0"), False)
    is_correct(is_ipv4_address("1.1.1.1a"), False)
    is_correct(is_ipv4_address("1"), False)
    is_correct(is_ipv4_address("0.254.255.0"), True)
    is_correct(is_ipv4_address("1.23.256.255."), False)
    is_correct(is_ipv4_address("1.23.256.."), False)
    is_correct(is_ipv4_address("0..1.0"), False)
    is_correct(is_ipv4_address("64.233.161.00"), False)
    is_correct(is_ipv4_address("64.00.161.131"), False)
    is_correct(is_ipv4_address("01.233.161.131"), False)
    is_correct(is_ipv4_address("35..36.9.9.0"), False)
    is_correct(is_ipv4_address("1.1.1.1.1"), False)
    is_correct(is_ipv4_address("1.256.1.1"), False)
    is_correct(is_ipv4_address("a0.1.1.1"), False)
    is_correct(is_ipv4_address("0.1.1.256"), False)
    is_correct(is_ipv4_address("129380129831213981.255.255.255"), False)
    is_correct(is_ipv4_address("255.255.255.255abcdekjhf"), False)
    is_correct(is_ipv4_address("7283728"), False)
    is_correct(is_ipv4_address("00001.100.1.10.m0"), False)
    is_correct(is_ipv4_address("111222333444"), False)
    is_correct(is_ipv4_address("0..1.0.0"), False)
    is_correct(is_ipv4_address("1.1.1.1"), True)
    is_correct(is_ipv4_address("255.255.255.255"), True)
    end_pit = time.clock()
    res_pit = end_pit - start_pit
    print("\nis_ipv4_address_built_in function:")
    start_b = time.clock()
    is_correct(is_ipv4_address_built_in("172.16.254.1"), True)
    is_correct(is_ipv4_address_built_in("172.316.254.1"), False)
    is_correct(is_ipv4_address_built_in(".254.255.0"), False)
    is_correct(is_ipv4_address_built_in("1.1.1.1a"), False)
    is_correct(is_ipv4_address_built_in("1"), False)
    is_correct(is_ipv4_address_built_in("0.254.255.0"), True)
    is_correct(is_ipv4_address_built_in("1.23.256.255."), False)
    is_correct(is_ipv4_address_built_in("1.23.256.."), False)
    is_correct(is_ipv4_address_built_in("0..1.0"), False)
    is_correct(is_ipv4_address_built_in("64.233.161.00"), False)
    is_correct(is_ipv4_address_built_in("64.00.161.131"), False)
    is_correct(is_ipv4_address_built_in("01.233.161.131"), False)
    is_correct(is_ipv4_address_built_in("35..36.9.9.0"), False)
    is_correct(is_ipv4_address_built_in("1.1.1.1.1"), False)
    is_correct(is_ipv4_address_built_in("1.256.1.1"), False)
    is_correct(is_ipv4_address_built_in("a0.1.1.1"), False)
    is_correct(is_ipv4_address_built_in("0.1.1.256"), False)
    is_correct(is_ipv4_address_built_in("129380129831213981.255.255.255"), False)
    is_correct(is_ipv4_address_built_in("255.255.255.255abcdekjhf"), False)
    is_correct(is_ipv4_address_built_in("7283728"), False)
    is_correct(is_ipv4_address_built_in("00001.100.1.10.m0"), False)
    is_correct(is_ipv4_address_built_in("111222333444"), False)
    is_correct(is_ipv4_address_built_in("0..1.0.0"), False)
    is_correct(is_ipv4_address_built_in("1.1.1.1"), True)
    is_correct(is_ipv4_address_built_in("255.255.255.255"), True)
    end_b = time.clock()
    res_b = end_b - start_b
    print("\npit time:\t\t{} sec\nbuilt-in time:\t{} sec".format(res_pit, res_b))
