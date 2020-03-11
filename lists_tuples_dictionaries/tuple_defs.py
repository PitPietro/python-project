"""
Global tuple to avoid make a new one each time a method is called
"""
my_tuple = ("London", 123, 18.2)


def city_tuple_declaration():
    city = ("Rome", "London", "Tokyo")
    return city


def tuple_get_element(index: int):
    try:
        element = my_tuple[index]
        print(element)
    except IndexError:
        print("index {} out of range".format(index))


def tuple_has_element(element: str) -> bool:
    answer = element in my_tuple
    return answer


def tuple_has_not_element(element: str) -> bool:
    answer = element not in my_tuple
    return answer


def bool_to_string_translator(answer: bool) -> str:
    if answer:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    main_tuple = city_tuple_declaration()
    print(main_tuple)
    print(my_tuple)
    tuple_get_element(5)
    print(bool_to_string_translator(tuple_has_element("London")))
    print(bool_to_string_translator(tuple_has_not_element("London")))
