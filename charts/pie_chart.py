import matplotlib.pyplot as plt


my_dict = {'Python': 30, 'C#': 10, 'Java': 40, 'Perl': 20}


def pie_1():
    # Data to plot
    colors = ['gold', 'yellowgreen', 'red', 'lightskyblue']
    explode = (0.1, 0.1, 0.1, 0.1)  # explode 1st slice

    # Plot
    plt.pie(
        my_dict.values(),
        explode=explode,
        labels=my_dict.keys(),
        colors=colors,
        autopct='%1.1f%%',
        shadow=True,
        startangle=0)

    plt.axis('equal')
    plt.show()


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)
    return my_autopct


def pie_2_autopct():
    plt.pie(
        my_dict.values(),
        labels=my_dict.keys(),
        autopct=make_autopct(my_dict.values())
    )
    plt.show()


if __name__ == '__main__':
    s = 2
    # int(input('Which Chart do you want to see? '))
    if s == 1:
        pie_1()
    elif s == 2:
        pie_2_autopct()
