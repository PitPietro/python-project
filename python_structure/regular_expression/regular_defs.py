import re

zen = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


def one_word_in_a_line(word, line):
    """

    :param word: the word the regular expression will search
    :param line: the string the regular expression will search 'word' in
    :return: the list of matches
    """
    return re.findall(word, line)


def one_word_in_a_line_ignore_case(word, line):
    """
    'one_word_in_a_line' but no keys sensitive
    :param word: the word the regular expression will search
    :param line: the string the regular expression will search 'word' in
    :return: the list of matches
    """
    return re.findall(word, line, re.IGNORECASE)


def start_with(word, line):
    word = "^" + word
    return re.findall(word, line)


def start_with_multiline(word, line):
    word = "^" + word
    return re.findall(word, line, re.MULTILINE)


def end_with(word, line):
    word = word + "$"
    return re.findall(word, line)


def find_digit(line):
    """
    The '\d' search for the digit in 'line'
    :param line:
    :return:
    """
    return re.findall("\d", line, re.IGNORECASE)


if __name__ == '__main__':
    print(one_word_in_a_line("Pit", "I'm working whit Pit"))
    print(one_word_in_a_line_ignore_case("Pit", "Pit is digging a pit"))
    print(start_with("Are", "Are you kidding me?"))
    print(start_with_multiline("If", zen))
    print(end_with("funny!", "Sometimes you are funny!"))
    print(find_digit("12"))
