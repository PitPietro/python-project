"""
https://pypi.org/project/tqdm/#manual
"""
from tqdm import tqdm, trange
from time import sleep


def manual_1():
    with tqdm(total=100) as pbar:
        for i in range(10):
            sleep(0.1)
            pbar.update(10)


def manual_2():
    progress_bar_2 = tqdm(total=100)
    for i in range(10):
        sleep(0.1)
        progress_bar_2.update(10)
    progress_bar_2.close()


if __name__ == '__main__':
    manual_1()
    manual_2()
