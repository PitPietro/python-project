def bubble_sort(num_list):
    """
    https://stackabuse.com/sorting-algorithms-in-python/
    :param num_list:
    :return:
    """
    swap = True
    while swap:
        swap = False
        for i in range(len(num_list) - 1):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
                swap = True
    return num_list


if __name__ == '__main__':
    n1 = [8, 7, 56, 1, 9]
    print(n1)
    bubble_sort(n1)
    print(n1)
