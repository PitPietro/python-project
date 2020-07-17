import matplotlib.pyplot as plt

"""
https://matplotlib.org/gallery/lines_bars_and_markers/broken_barh.html#sphx-glr-gallery-lines-bars-and-markers-broken-barh-py
"""


def broken_b_1():
    fig, ax = plt.subplots()
    ax.broken_barh(
        [(110, 30), (150, 10)],
        (10, 9),
        facecolors='tab:blue'
    )
    ax.broken_barh(
        [(10, 50), (100, 20), (130, 10)],
        (20, 9),
        facecolors=('tab:orange', 'tab:green', 'tab:red')
    )
    ax.set_ylim(5, 35)
    ax.set_xlim(0, 200)
    ax.set_xlabel('seconds since start')
    ax.set_yticks([15, 25])
    ax.set_yticklabels(['Bill', 'Jim'])
    ax.grid(True)
    ax.annotate(
        'race interrupted',
        (61, 25),
        xytext=(0.8, 0.9),
        textcoords='axes fraction',
        arrowprops=dict(facecolor='black', shrink=0.05),
        fontsize=16,
        horizontalalignment='right',
        verticalalignment='top'
    )

    plt.show()


if __name__ == '__main__':
    broken_b_1()
