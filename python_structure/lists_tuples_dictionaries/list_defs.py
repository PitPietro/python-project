star_wars_movies = ["Episode I - The Phantom Menace",
                    "Episode II – Attack of the Clones",
                    "Episode III – Revenge of the Sith",
                    "Episode IV – A New Hope",
                    "Episode V – The Empire Strikes Back",
                    "Episode VI – Return of the Jedi",
                    "Episode VII – The Force Awakens",
                    "Episode VIII – The Last Jedi",
                    "Episode IX – The Rise of Skywalker",
                    "Rogue One: A Star Wars Story",
                    "Solo: A Star Wars Story"]

rating_movies = ["I love Episode I",
                 "Episode II is nice",
                 "Episode III is quite good",
                 "Episode IV is super cool",
                 "Episode V is wonderful",
                 "Episode VI is super bad",
                 "I felt asleep during Episode VII",
                 "I watched Episode VIII two times",
                 "I didn't want to see Episode IX",
                 "Rogue One is a nice film",
                 "I didn't see Solo"]

num_rating_movies = [2, 3, 5, 10, 4, 1, 8, 9, 3, 2, 5]


def list_declaration_1(a="Mozart", b=1.2):
    """
    Lists are mutable
    :param a: optional parameter
    :param b: optional parameter
    :return: a declared list
    """
    artists = [a, b, "Caparezza", "Lety", "Pit", "Virgi"]

    print(artists)
    return artists


def list_append(my_list: list):
    user_input = input("Item to append to the list: ")
    my_list.append(user_input)
    print(my_list)
    return my_list


def list_sum(my_list: list):
    print("\nSum the parameter's list with another list")
    random_list = list("H7")
    random_list.append(45)
    sum_l = my_list + random_list
    print(sum_l)
    return sum_l


def list_change_element(my_list: list, index, new_element="default"):
    print("\nChange a list element with another one at a given index")
    my_list[index] = new_element
    return print(my_list)


def combine_two_lists(list_1, list_2):
    """
    Use the built-in 'zip' function: it takes two lists and
    combines the fist two elements into a tuple, than make the
    same thing for all the elements of the lists
    :param list_1:
    :param list_2:
    :return:
    """
    my_list = []
    for i in zip(list_1, list_2):
        my_list.append(i)
    return my_list


"""
List Comprehension
Allows to create lists based on criteria applied to existing lists.
1) Iterates
2) Processes
3) Filter
"""


def string_to_list(word):
    """
    Take each character of the 'word' parameter and return a list
    populated with all the characters
    :param word: string
    :return: list of string's characters
    """
    return [c for c in word]


def string_to_list_only_digit(word):
    """
    Take each character of the 'word' parameter and return a list
    populated with all the characters. The if clause allows only
    the digits to be added to the list.
    :param word: string
    :return: list of digit inside 'word'
    """
    return [c for c in word if c.isdigit()]


def string_to_list_only_last_digit(word):
    """
    The negative index allows to select only the last digit
    from the new list
    :param word: parameter
    :return: list
    """
    return [c for c in word if c.isdigit()][-1]


def multiply_list(multiplier, input_list):
    return [i * multiplier for i in input_list]


def list_intersection(list1, list2):
    """
    Check if each value in list1 is also in list2
    :param list1:
    :param list2:
    :return: a list containing the elements common to both the lists
    """
    return [value for value in list1 if value in list2]


def set_intersection(list1, list2):
    """
    Using the built-in 'intersection()' method form a 'set()' element.
    'intersection()' can have as parameters more than two sets.
    :param list1:
    :param list2:
    :return:
    """
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))


def find_the_single_element(my_list):
    """
    Given a non-empty list of integers, every element appears twice except for one. Find that single one.
    :param my_list:
    :return:
    """
    duplicates = []
    my_set = set()
    for i in my_list:
        length_one = len(my_set)
        my_set.add(i)
        length_two = len(my_set)
        if length_one == length_two:
            duplicates.append(i)

    return [i for i in my_list + duplicates if i not in my_list or i not in duplicates]
    # list_dif = []
    # for i in my_list + duplicates:
    #     if i not in my_list or i not in duplicates:
    #         list_dif.append(i)
    # return list_dif


def find_the_single_element_with_dict(my_list):
    count = {}
    for i in my_list:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    for key, value in count.items():
        if value == 1:
            return key


if __name__ == '__main__':
    main_artist = list_declaration_1("Aladino")
    # list_append(main_artist)
    s_list = list_sum(main_artist)
    list_change_element(s_list, 4)
    print("\n")
    print(combine_two_lists(star_wars_movies, rating_movies))
    my_s = "You 2 are good to be 43."
    print(string_to_list(my_s))
    print(string_to_list_only_digit(my_s))
    print(string_to_list_only_last_digit(my_s))
    my_n = [1, 7, 5, 3, 2]
    print(multiply_list(7, my_n))
    my_n2 = [1, 4, 3, 8]
    print(list_intersection(my_n, my_n2))
    print(set_intersection(my_n, my_n2))
    # find_the_single_element
    duplicates_list = [1, 2, 3, 2, 3, 1, 4]
    print(find_the_single_element(duplicates_list))
    print(find_the_single_element_with_dict(duplicates_list))
