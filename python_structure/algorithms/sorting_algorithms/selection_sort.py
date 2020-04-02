def selection_sort(num_list):
    for i in range(len(num_list)):
        print("{})".format(i))
        smallest = min(num_list[i:])
        index = num_list.index(smallest)
        print("smallest: {}    index: {}\nlist: {}".format(smallest, index, num_list))
        num_list[i], num_list[index] = num_list[index], num_list[i]
        print("smallest: {}    index: {}\nlist: {}\n".format(smallest, index, num_list))
    return num_list


if __name__ == '__main__':
    print(selection_sort([8, 99, 12, -1, 3]))
