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


if __name__ == '__main__':
    main_artist = list_declaration_1("Aladino")
    list_append(main_artist)
    s_list = list_sum(main_artist)
    list_change_element(s_list, 4)
    print("\n")
    print(combine_two_lists(star_wars_movies, rating_movies))
