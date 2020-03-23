import random
import time

from python_structure.data_structures.stacks_queues.stack import Stack
from python_structure.data_structures.stacks_queues.queue import Queue


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
            return my_name[n]
        except IndexError:
            return "index {} invalid".format(n)


def string_concatenation(a: str, b: str, c: str) -> str:
    """
    Concatenate the strings given as parameter and return the concatenation
    :param a: parameter
    :param b: parameter
    :param c: parameter
    :return: string concatenation
    """
    return a + b + c


def multiply_operator(word: str, factor: int = 1):
    """
    Multiply the string 'word' for the 'factor' value
    :param word: string to be multiplied
    :param factor: it's default value is 1
    :return: multiplied string
    """
    return word * factor


def to_upper(word: str):
    """
    Make the 'word' parameter uppercase
    :param word: string to be uppercase
    :return: uppercase string
    """
    return word.upper()


def to_lower(word: str):
    """
    Make the 'word' parameter lowercase
    :param word: string to be lowercase
    :return: lowercase string
    """
    return word.lower()


def to_capital(word: str):
    """
    Make the 'word' parameter capitalized
    :param word: string to be capitalized
    :return: capitalized string
    """
    return word.capitalize()


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
    :return: case-folded string
    """
    return word.casefold()


def to_swap_case(word: str):
    """
    The 'swapcase()' method converts all uppercase
    characters to lowercase and all lowercase characters
    to uppercase characters of the 'word' string.
    :param word: the string to be swapcased
    :return: the swap-cased string
    """
    return word.swapcase()


def to_format_params(name: str, city: str):
    """
    Take the 'name' and 'city' and put them in a formatted string
    :param name: parameter
    :param city: parameter
    :return: formatted string
    """
    return "I'm {} years old and I'm from {}".format(name, city)


def to_format(phrase: str, param: str):
    """
    The 'phrase' string is formatted taking 'param' parameter
    :param phrase: it must contain a {} that will be replaced by the 'param' parameter
    :param param: parameter
    :return: formatted string
    """
    return phrase.format(param)


def split_string(phrase: str, split_param: str):
    """
    Split the 'phrase' string in different strings taking 'split_param' as split's parameter
    :param phrase: string to be splitted
    :param split_param: split's parameter
    :return: a list of strings
    """
    return phrase.split(split_param)


def join_string(phrase: str, join_s: str):
    """
    Take the 'phrase' and intersperse it whit 'join_s' string
    :param phrase: string to be interspersed
    :param join_s: string
    :return: interspersed string
    """
    return join_s.join(phrase)


def join_list(words: list, join_s: str):
    """
    Take each strings in the list 'words' is joined in a single string spaced whit 'join_s'
    :param words: string to be joined
    :param join_s: spaced string
    :return: joined string
    """
    return join_s.join(words)


def strip_string(phrase: str):
    """
    The strip method removes leading and trailing whitespace from a string
    :param phrase:
    :return:
    """
    return phrase.strip()


def to_slice_string(phrase: str, start: int, end: int):
    """
    Slicing returns a new iterable from a subset of the items in the 'phrase' string
    :param phrase: string to be sliced
    :param start: it is included in the sliced elements and, if it's equal to zero, can be omitted
    :param end: it isn't included in the sliced elements and, if it's equal to le length of 'phrase', can be omitted
    :return: sliced string
    """
    return phrase[start:end]


def to_slice_list(my_list: list, start: int, end: int):
    """
    Slicing returns a new iterable from a subset of the items in the 'phrase' string
    :param my_list: list to be sliced
    :param start: it is included in the sliced elements and, if it's equal to zero, can be omitted
    :param end: it isn't included in the sliced elements and, if it's equal to le length of 'phrase', can be omitted
    :return: sliced list
    """
    return my_list[start:end]


def replace_in_string(phrase: str, l_to_replace: str, replacement: str):
    """
    Take the 'phrase' string and replace all the 'l_to_replace' occurrence whit 'replacement' string
    :param phrase: string that will be modified
    :param l_to_replace: string to be replaced
    :param replacement: string that will replace 'l_to_replace'
    :return: 'phrase' string modified
    """
    return phrase.replace(l_to_replace, replacement)


def find_index(phrase: str, letter: str) -> int:
    """
    Find the 'phrase' index at the first occurrence of 'letter' string
    :param phrase: string where the index will be found on
    :param letter: index occurrence
    :return: integer corresponding to 'letter' position
    """

    try:
        return phrase.index(letter)
    except ValueError:
        return -1


def reverse_string(string):
    """
    Reverse the given string by adding each element to a stack with a for-loop.
    Then use the 'pop' function of the stack for each element of the stack
    to get the items from the last to the first and append to a new string variable.
    :param string: a string
    :return: reversed 'string'
    """
    stack = Stack()
    for i in string:
        stack.push(i)

    reversed_s = ""
    for i in range(stack.size()):
        reversed_s += stack.pop()

    return reversed_s


def simulate_line(till_show, max_time):
    """
    Simulate people wait in line to buy tickets for a movie
    :param till_show: time until the movie starts
    :param max_time: the longest time it can take to a person to purchase a ticket
    :return: tickets that have been sold
    """
    people = Queue()
    tickets_sold = []

    for i in range(10):
        people.enqueue("Bill" + str(i))

    tickets_end = time.time() + till_show
    now = time.time()
    while now < tickets_end and not people.is_empty():
        now = time.time()
        rand = random.randint(0, max_time)
        time.sleep(rand)
        person = people.dequeue()
        print("Ticket sold to ", person)
        tickets_sold.append(person)

    return tickets_sold


if __name__ == '__main__':
    negative_index()
    my_string = "I am meeting some friends. They're very interesting"
    letter_y = "y"

    print("\n" + string_concatenation("Hi ", "how ", "are you?"))
    print(multiply_operator("Hello", 4))
    print(to_case_fold("Why? ß "))
    print(to_swap_case("I am nOt sTuPid"))
    print(to_format_params("18", "Florence"))
    print(split_string(my_string, ". "))
    print(join_string("Pit", "-"))

    l_words = ["Peter", "is", "reading", "a", "book"]
    print(join_list(l_words, " "))
    print(strip_string("  Pit  "))

    print(to_capital("white"))
    print(to_slice_string("I'm good", 1, 5))
    print(to_slice_list(l_words, 2, 4))
    print(replace_in_string(my_string, "e", "€"))

    print("The letter {} is at index {}".format(letter_y, find_index(my_string, "z")))
    print(reverse_string("Hello"))
    print("\n",simulate_line(20, 2))
