import matplotlib.pyplot as plt

"""
https://matplotlib.org/gallery/lines_bars_and_markers/categorical_variables.html#sphx-glr-gallery-lines-bars-and-markers-categorical-variables-py
"""


def plotting_1():
    data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
    names = list(data.keys())
    values = list(data.values())

    fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
    axs[0].bar(names, values)
    axs[1].scatter(names, values)
    axs[2].plot(names, values)
    fig.suptitle('Categorical Plotting')
    plt.show()


def plotting_2():
    up = '1'
    down = '0'
    file_1_list = [up, down, up, up, down, up]
    file_2_list = [down, down, down, up, up, up]
    activity = ["bit 1", "bit 2", "bit 3", "bit 4", "bit 5", "bit 6"]

    fig, ax = plt.subplots()
    ax.plot(activity, file_1_list, label="file 1")
    ax.plot(activity, file_2_list, label="file 2")
    ax.legend()

    plt.show()


if __name__ == '__main__':
    s = 1
    # int(input('Which Chart do you want to see? '))
    if s == 1:
        plotting_1()
    elif s == 2:
        plotting_2()
