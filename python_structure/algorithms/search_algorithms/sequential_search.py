def sequential_search(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found


if __name__ == '__main__':
    my_list = range(1, 1000)
    seq_s = sequential_search(my_list, 1889)
    print(seq_s)
