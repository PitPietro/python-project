"""
Binary Search:
It is a series of iterations that divide a sorted list
in halt until it find a specific element
"""


def binary_search_return_bool(s_list, item):
    first = 0
    last = len(s_list)-1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if s_list[mid] == item:
            found = True
        elif item < s_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return found


def binary_search_return_index(s_list, item):
    first = 0
    last = len(s_list)-1
    while first <= last:
        mid = (first + last) // 2
        if s_list[mid] == item:
            return mid
        elif item < s_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return None


def bool_translator(my_bool):
    if my_bool:
        return "Yes!"
    else:
        return "No!"


if __name__ == '__main__':
    my_list = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    element = 8
    b_result = binary_search_return_bool(my_list, element)
    str_result = bool_translator(b_result)
    print("Given the list {}\nDoes {} is owned by the list? {}".format(my_list, element, str_result))
    index_result = binary_search_return_index(my_list, element)
    print("{} is at index {}".format(element, index_result))
