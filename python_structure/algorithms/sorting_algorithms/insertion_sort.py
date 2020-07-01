def insertion_sort_log(num_list):
    """
    Start the for loop on the second element (the number 1) as it's assumed that
    the first element is sorted. 'j' keeps a reference of the previous element's index.
    The while loop moves all items of the sorted segment forward if they are larger than
    the item to insert. After the loop, insert the element.
    The 'log' version of the algorithm has some print statements.
    :param num_list: unordered list of integer
    :return: ordered list of integer
    """
    for i in range(1, len(num_list)):
        item_to_insert = num_list[i]
        j = i - 1
        print("item to insert: {}    prev element's index: {}".format(item_to_insert, j))
        while j >= 0 and num_list[j] > item_to_insert:
            print("while {} >= 0 and {} > {} :".format(j, num_list[j], item_to_insert))
            num_list[j + 1] = num_list[j]
            print("num_list[{}]: {} = num_list[{}]: {}".format(j+1, num_list[j+1], j, num_list[j]))
            j -= 1
            print("j -= 1 -> {}".format(j))
            print(num_list)
        num_list[j + 1] = item_to_insert
        print("num_list[{}]: {} = item to insert: {}".format(j+1, num_list[j+1], item_to_insert))
        print(num_list)
    return num_list


if __name__ == '__main__':
    a = [9, 1, 15, 28, 6]
    print(a)
    print(insertion_sort_log(a))
