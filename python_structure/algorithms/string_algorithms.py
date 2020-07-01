def is_palindrome(word):
    """
    Reverse the entire word by slicing it all. Compare the reversed word
    with the original word.
    :param word:
    :return:
    """
    word = word.lower()
    return word[::-1] == word


def is_anagram(word_1, word_2):
    """
    Test if the parameters are anagram of themselves.
    :param word_1: 1st word
    :param word_2: 2nd word
    :return: True if the parameters are anagram, False if not
    """
    word_1.lower()
    word_2.lower()
    return sorted(word_1) == sorted(word_2)


def count_characters(string):
    """
    Count how many times each character occurs in the given parameters
    :param string:
    :return: a dictionary where each key is a character and each value
    is the number of times it occurred in the string
    """
    string = string.lower()
    count_dictionary = {}
    for i in string:
        if i in count_dictionary:
            count_dictionary[i] += 1
        else:
            count_dictionary[i] = 1
    print(count_dictionary)


if __name__ == '__main__':
    r = is_palindrome("Anna")
    print(r)
    a = is_anagram("cinema", "iceman")
    print(a)
    count_characters("Hello")
