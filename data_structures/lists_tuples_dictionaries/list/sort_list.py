def sort_list(my_list):
    my_list.sort()


def sort_lower(my_list):
    my_list.sort(key=str.lower)


def sort_upper(my_list):
    my_list.sort(key=str.upper)


if __name__ == '__main__':
    num_l = [44, 5.9, 33, 2]
    str_l = ['Zorro', 'You', 'Car', 'Alpha']

    print(num_l)
    print(str_l)

    sort_list(num_l)
    sort_list(str_l)

    print(num_l)
    print(str_l, end='\n\n')

    a_z = ['a', 'z', 'A', 'Z']
    print(a_z, '\t unsorted')
    sort_list(a_z)
    print(a_z, '\t normal sort')

    a_z = ['a', 'z', 'A', 'Z']
    sort_lower(a_z)
    print(a_z, '\t key=str.lower')

    a_z = ['a', 'z', 'A', 'Z']
    sort_upper(a_z)
    print(a_z, '\t key=str.upper')
