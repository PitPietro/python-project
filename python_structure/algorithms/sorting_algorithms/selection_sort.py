def selection_sort(num_list):
    for i in range(len(num_list)):
        print("{})".format(i))
        smallest = min(num_list[i:])
        index = num_list.index(smallest)
        num_list[i], num_list[index] = num_list[index], num_list[i]

    return num_list


def selection_sort_v2(num_list):
    # i corresponds to how many values were sorted
    for i in range(len(num_list)):
        # assuming that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # the loop iterates over the unsorted items
        for j in range(i + 1, len(num_list)):
            if num_list[j] < num_list[lowest_value_index]:
                lowest_value_index = j
        # swap values of the lowest unsorted element with the first unsorted element
        num_list[i], num_list[lowest_value_index] = num_list[lowest_value_index], num_list[i]
    return num_list


if __name__ == '__main__':
    a = [8, 99, 12, -1, 3]
    print(selection_sort(a))
    print(selection_sort_v2(a))
