def tuples_cities_inside_list():
    locations = []

    # the tuples store the longitude and latitude of the cities
    la = (34.0522, 188.2437)
    chicago = (41.8781, 87.6298)

    # append the tuples to the location list
    locations.append(la)
    locations.append(chicago)

    print(locations)


def lists_author_inside_tuple():
    eights = ["E. A. Poe", "C. Dickens"]

    nines = ["Hemingway",
             "Fitzgerald",
             "Orwell"]

    authors = (eights, nines)
    print(authors)

    """
    'lists' and 'elements' are not integer, unlike in the for loops
    in Java: they are strings and represent the lists' elements
    """
    for lists in authors:
        for elements in lists:
            print(elements)


def nested_dictionary_ny():
    ny = {
        "location":
            (40.7128,
             74.0059),

        "celebs":
            ["W. Allen",
             "Jay Z",
             "K. Bacon"],

        "facts":
            {"state": "NY",
             "country": "America"}
    }

    print(ny)


if __name__ == '__main__':
    tuples_cities_inside_list()
    lists_author_inside_tuple()
    nested_dictionary_ny()
