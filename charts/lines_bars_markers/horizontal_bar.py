import matplotlib.pyplot as plt
import numpy as np

"""
https://matplotlib.org/gallery/lines_bars_and_markers/barh.html#sphx-glr-gallery-lines-bars-and-markers-barh-py
"""


def horizontal_1():
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data
    people = ('Tom', 'John', 'Violette', 'Arthur', 'Cece')
    y_pos = np.arange(len(people))
    performance = 3 + 10 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)

    # labels read top-to-bottom
    ax.invert_yaxis()
    ax.set_xlabel('Performance')
    ax.set_title('People\'s speed on the crosswalk:')

    plt.show()


if __name__ == '__main__':
    horizontal_1()
