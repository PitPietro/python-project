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


def is_ipv4_address(ip):
    range_n = [0, 255]
    if len(ip) > 5:
        return True
    else:
        return False


def is_correct(def_res, result):
    if def_res == result:
        print("Correct")
    else:
        print("INCORRECT")


if __name__ == '__main__':
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
    is_correct(is_ipv4_address("0..1.0.0"), False)
