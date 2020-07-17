import random

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


def pie_3_legend():
    """
    |-- Location String --|-- Location Code --|
    |---------------------|-------------------|
    |-- 'best' 	        --|--       0       --|
    |-- 'upper right'   --|--    	1       --|
    |-- 'upper left' 	--|--       2       --|
    |-- 'lower left' 	--|--       3       --|
    |-- 'lower right' 	--|--       4       --|
    |-- 'right' 	    --|--       5       --|
    |-- 'center left' 	--|--       6       --|
    |-- 'center right' 	--|--       7       --|
    |-- 'lower center' 	--|--       8       --|
    |-- 'upper center' 	--|--       9       --|
    |-- 'center' 	    --|--      10       --|
    |-----------------------------------------|
    :return: 3rd plot
    """
    plt.pie(
        my_dict.values(),
        labels=my_dict.keys(),
        autopct='%0.2f%%'
    )
    loc_dict = {'best': 0,
                'upper right': 1,
                'upper left': 2,
                'lower left': 3,
                'lower right': 4,
                'right': 5,
                'center left': 6,
                'center right': 7,
                'lower center': 8,
                'upper center': 9,
                'center': 10}
    random_legend = random.choice(list(loc_dict.values()))
    print('Legend position: ', list(loc_dict.keys())[list(loc_dict.values()).index(random_legend)])
    plt.legend(my_dict.keys(), loc=random_legend)
    plt.show()


if __name__ == '__main__':
    s = 3
    # int(input('Which Chart do you want to see? '))
    if s == 1:
        pie_1()
    elif s == 2:
        pie_2_autopct()
    elif s == 3:
        pie_3_legend()
