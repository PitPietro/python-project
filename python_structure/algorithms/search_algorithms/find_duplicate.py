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


if __name__ == '__main__':
    my_list = ["Pit", "Pat", "Pot", "Pit"]
    result = return_duplicates(my_list)
    print(result)
