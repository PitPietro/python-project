from subprocess import check_output

import psutil as psutil


def get_pid(name):
    return check_output(["pidof", name])


def kill_pid(num):
    for pid in num:
        print(pid)
        i_pid = int(pid)
        p = psutil.Process(i_pid)
        p.terminate()


if __name__ == '__main__':
    value = check_output(["pidof", "Typora"])
    print(value)
    value = value[:-1]
    s_value = value.split(b' ')
    print(s_value)
    kill_pid(s_value)
