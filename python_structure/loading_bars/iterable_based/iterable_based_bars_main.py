"""
https://pypi.org/project/tqdm/#iterable-based
"""
from tqdm import tqdm, trange
from time import sleep


def iterable_1():
    text = ""
    for char in tqdm(["a", "b", "c", "d"]):
        sleep(0.5)
        text = text + char


def iterable_2():
    pbar = tqdm(["a", "b", "c", "d"])
    for char in pbar:
        sleep(0.25)
        pbar.set_description("Processing %s" % char)


if __name__ == '__main__':
    iterable_1()
    iterable_2()
