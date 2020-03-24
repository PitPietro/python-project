def return_duplicates(d_list):
    """
    A 'set()' is a kind of list that can not have duplicates.
    Steps to follow to return the duplicates of a list:
    1) create an empty list
    2) create an empty set
    3) Step through each item in the list by using a for-loop
    4) Get the length of the set
    5) Attempt to add an item from the list into the set
    6) Get the new length of the set
    7) Compare the two lengths: if they are the same, the item is a duplicate
    8) Append the duplicate item to the list of duplicates
    9) At the end of the loop, return the list of duplicates
    :param d_list: the list
    :return: list of duplicates
    """
    duplicates = []
    my_set = set()
    for i in d_list:
        length_one = len(my_set)
        my_set.add(i)
        length_two = len(my_set)
        if length_one == length_two:
            duplicates.append(i)
    return duplicates


def return_first_duplicate(d_list):
    """
    Given an array a that contains only numbers in the range from 1 to 'd_list'.length, find the
    first duplicate number for which the second occurrence has the minimal index. In other words,
    if there are more than 1 duplicated numbers, return the number for which the second occurrence
    has a smaller index than the second occurrence of the other number does.
    If there are no such elements, return -1.
    :param d_list:
    :return:
    """
    duplicate = -1
    my_set = set()
    for i in d_list:
        length_one = len(my_set)
        my_set.add(i)
        length_two = len(my_set)
        if length_one == length_two:
            return i
    return duplicate


if __name__ == '__main__':
    my_list = ["Pit", "Pat", "Pot", "Pit"]
    my_digit = [2, 1, 3, 5, 3, 2]
    result = return_duplicates(my_list)
    print(result)
    res_2 = return_first_duplicate(my_digit)
    print(res_2)
