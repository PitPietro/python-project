def negative_index():
    """
    Python allows to use negative index to look up at the elements
    inside a string, from right to left: 'my_name[-1]' will take the
    last element of 'my_name'.
    :return:
    """
    my_name = "Peter"
    number_list = [-1, -2, -3, -4, -5, -6, 0, 1, 2, 3, 4, 5]
    print(my_name)
    for n in number_list:
        try:
            print(my_name[n])
        except IndexError:
            print("index {} invalid".format(n))


def string_concatenation(a: str, b: str, c: str) -> str:
    return a + b + c


def multiply_operator(word: str, factor: int = 1):
    print(word * factor)


def to_upper(word: str):
    print(word.upper())


def to_lower(word: str):
    print(word.lower())


def to_capital(word: str):
    print(word.capitalize())


def to_case_fold(word: str):
    """
    The casefold() method is an aggressive lower() method which
    convert strings to casefolded strings for caseless matching.
    The casefold() method is removes all case distinctions
    present in a string. It is used for caseless matching
    (i.e. ignores cases when comparing).
    For example, German lowercase letter ß is equivalent to ss.
    However, since ß is already lowercase, lower() method
    does nothing to it. But, casefold() converts it to ss.
    :param word: the string to be casefolded
    :return: the casefolded
    """
    print(word.casefold())


def to_swap_case(word: str):
    """
    The string swapcase() method converts all uppercase
    characters to lowercase and all lowercase characters
    to uppercase characters of the given string, and returns it.
    :param word: the string to be swapcased
    :return: the swapcased string
    """
    print(word.swapcase())


def to_format(name: str, city: str):
    print("I'm {} years old and I'm from {}".format(name, city))


def split_string(phrase: str, split_param: str):
    print(phrase.split(split_param))


def join_string(phrase: str, join_s: str):
    result = join_s.join(phrase)
    print(result)


def join_list(words: list, join_s):
    result = join_s.join(words)
    print(result)


def strip_string(phrase: str):
    """
    The strip method removes leading and trailing whitespace from a string
    :param phrase:
    :return:
    """
    print(phrase.strip())


def to_slice_string(phrase: str, start: int, end: int):
    """
    Slicing returns a new iterable from a subset of the items in the 'phrase' string
    :param phrase:
    :param start: it is included in the sliced elements and, if it's equal to zero, can be omitted
    :param end: it isn't included in the sliced elements and, if it's equal to le length of 'phrase', can be omitted
    :return:
    """
    result = phrase[start:end]
    print(result)


def to_slice_list(my_list: list, start: int, end: int):
    result = my_list[start:end]
    print(result)


def replace_in_string(phrase: str, l_to_replace: str, replacement: str):
    return phrase.replace(l_to_replace, replacement)


def find_index(phrase: str, letter: str) -> int:
    return phrase.index(letter)


if __name__ == '__main__':
    negative_index()
    my_string = "I am meeting some friends. They're very interesting"
    letter_y = "y"

    print("\n" + string_concatenation("Hi ", "how ", "are you?"))
    multiply_operator("Hello", 4)
    to_case_fold("Why? ß ")
    to_swap_case("I am nOt sTuPid")
    to_format("18", "Florence")
    split_string(my_string, ". ")
    join_string("Pit", "-")

    l_words = ["Peter", "is", "reading", "a", "book"]
    join_list(l_words, " ")
    strip_string("  Pit  ")

    to_capital("white")
    to_slice_string("I'm good", 1, 5)
    to_slice_list(l_words, 2, 4)
    print(replace_in_string(my_string, "e", "€"))

    print("The letter {} is at index {}".format(letter_y, find_index(my_string, letter_y)))
