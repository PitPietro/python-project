import matplotlib.pyplot as plt


"""
https://matplotlib.org/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py
"""


def stacked_1():
    labels = ['P1', 'P2', 'P3', 'P4', 'P5']
    men_means = [20, 15, 22, 33, 10]
    women_means = [23, 18, 32, 21, 30]
    men_std = [2, 3, 4, 1, 2]
    women_std = [3, 5, 2, 3, 3]
    # the width of the bars: can also be len(x) sequence
    width = 0.4

    fig, ax = plt.subplots()

    ax.bar(labels, men_means, width, yerr=men_std, label='Men')
    ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means, label='Women')

    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.legend()

    plt.show()


if __name__ == '__main__':
    print('''\nThis is an example of creating a stacked bar plot with error bars using bar.
    Note the parameters yerr used for error bars, and bottom to stack the women's bars on top of the men's bars.''')
    stacked_1()
