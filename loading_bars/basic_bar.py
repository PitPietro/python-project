from tqdm import tqdm
import time


def basic_bar_1():
    for i in tqdm(
            range(100),
            desc="Loading ",
            ascii=False,
            ncols=75):
        time.sleep(0.1)
    print("Loading Complete")


def ascii_bar():
    for i in tqdm(
        range(100),
        ascii=True,
        ncols=100
    ):
        time.sleep(0.2)
    print("Ascii bar completed")


if __name__ == '__main__':
    ascii_bar()
    time.sleep(1)
    basic_bar_1()
