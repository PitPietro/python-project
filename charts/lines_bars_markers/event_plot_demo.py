import numpy as np
import matplotlib.pyplot as plt
import matplotlib

"""
https://matplotlib.org/gallery/lines_bars_and_markers/eventplot_demo.html#sphx-glr-gallery-lines-bars-and-markers-eventplot-demo-py
"""


def event_plot():
    matplotlib.rcParams['font.size'] = 8.0

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # create random data
    data1 = np.random.random([6, 50])

    # set different colors for each set of positions
    colors1 = ['C{}'.format(i) for i in range(6)]

    # set different line properties for each set of positions
    # note that some overlap
    line_offsets1 = [-15, -3, 1, 1.5, 6, 10]
    line_lengths1 = [5, 2, 1, 1, 3, 1.5]

    fig, axs = plt.subplots(2, 2)

    # create a horizontal plot
    axs[0, 0].eventplot(
        data1,
        colors=colors1,
        lineoffsets=line_offsets1,
        linelengths=line_lengths1
    )

    # create a vertical plot
    axs[1, 0].eventplot(
        data1,
        colors=colors1,
        lineoffsets=line_offsets1,
        linelengths=line_lengths1,
        orientation='vertical'
    )

    # create another set of random data.
    # the gamma distribution is only used for aesthetic purposes
    data2 = np.random.gamma(4, size=[60, 50])

    # use individual values for the parameters this time
    # these values will be used for all data sets (except lineoffsets2, which
    # sets the increment between each data set in this usage)
    colors2 = 'black'
    line_offsets2 = 1
    line_lengths2 = 1

    # create a horizontal plot
    axs[0, 1].eventplot(
        data2,
        colors=colors2,
        lineoffsets=line_offsets2,
        linelengths=line_lengths2
    )

    # create a vertical plot
    axs[1, 1].eventplot(
        data2,
        colors=colors2,
        lineoffsets=line_offsets2,
        linelengths=line_lengths2,
        orientation='vertical')

    plt.show()


if __name__ == '__main__':
    event_plot()
