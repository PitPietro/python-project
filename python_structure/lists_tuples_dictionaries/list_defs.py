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


if __name__ == '__main__':
    main_artist = list_declaration_1("Aladino")
    list_append(main_artist)
    s_list = list_sum(main_artist)
    list_change_element(s_list, 4)
