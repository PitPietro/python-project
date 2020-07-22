import re

# https://www.tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html#chap_04

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

text = """Giraffes have aroused
 the curiosity of __PLURAL_NOUN__
 since earliest times. The
 giraffe is the tallest of all
 living __PLURAL_NOUN__, but scientists
 are unable to explain
 how it got its long __PART_OF_THE_BODY__.
 The giraffe's tremendous
 height, which might reach
 __NUMBER__ __PLURAL_NOUN__, comes
 from it legs and __BODYPART__.
"""

underscores_words = "_one_ _two_ _three_"


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


def pipe_search():
    start_regex = re.compile(r'Bat(mobile|copter|bat)')
    result = start_regex.search('I am on a Batmobile')
    return result.group()


def start_with_multiline(word, line):
    word = "^" + word
    return re.findall(word, line, re.MULTILINE)


def end_with(word, line):
    word = word + "$"
    return re.findall(word, line)


def find_digit(line):
    """
    The d search for the digit in 'line'
    :param line:
    :return:
    """
    return re.findall('\d', line, re.IGNORECASE)


def greedy_match(word):
    """
    The period matches any character, so this regular expression
    matches any character between the underscores. To match as much
    text as possible, it will have to use the asterisk.
    :param word:
    :return:
    """
    return re.findall("_.*_", word)


def non_greedy_match_question_mark(word):
    """
    The period matches any character, so this regular expression
    matches any character between the underscores. To match as much
    text as possible, it will have to use the asterisk.
    :param word:
    :return:
    """
    return re.findall('_.*?_', word)


def mad_libs(mls):
    """
    'mls' must contains hints surrounded by double underscores.
    'findall' with non-greedy matching finds all the hints, then
    loop through them and display the hints to the user. The input
    function collects their answers. Replace each hand with the answer
    in the original text.
    :param mls: game's text
    :return:
    """
    print("\nGAME: Mad Libs")
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "Enter a {} ".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print("\n")
        # mls = mls.replace("\n", "")
        print(mls)
    else:
        print("invalid mls")


def zero_or_one_time():
    my_regex = re.compile(r'Bat(wo)?man')
    msg = 'The life of Batwoman'
    result = my_regex.search(msg)
    return return_result(result)


def zero_or_more():
    my_regex = re.compile(r'Bat(wo)*man')
    msg = 'The life of Batwowowoman'
    result = my_regex.search(msg)
    return return_result(result)


def one_or_more():
    my_regex = re.compile(r'Bat(wo)+man')
    msg = 'The life of Batman'
    result = my_regex.search(msg)
    return return_result(result)


def return_result(result):
    if result is None:
        return 'Did not find any match'
    else:
        return result.group()


def find_repetition(msg, word, num):
    # re.compile(r'(word){num}')
    regex = re.compile(r'(' + word + '){' + str(num) + '}')
    result = regex.search(msg)
    return return_result(result)


def find_repetition_range(msg, word, num_min, num_max):
    # re.compile(r'(word){min, max}')
    regex = re.compile(r'(' + word + '){' + str(num_min) + ',' + str(num_max) + '}')
    result = regex.search(msg)
    return return_result(result)


def only_digit():
    # the entire string must begin and end with digits only (no chars no spaces, nothing else)
    regex = re.compile(r'^\d+$')
    return return_result(regex.search('423431432'))


def any_chars():
    # the dot is looking for a single char --> re.compile(r'.@')
    regex = re.compile(r'.{1,3}@')
    msg = 'My emails are: pit@github.com and bob@gmail.com'
    return regex.findall(msg)


def any_names():
    regex = re.compile(r'First Name: (.*)\n Last Name: (.*)')
    # msg = 'First Name: {}\n Last Name: {}'.format(input('Name: '), input('Last name: '))
    msg = 'First Name: Pit\n Last Name: Pietro'
    return regex.findall(msg)


def replace_names():
    msg = 'Mr Banker gave my a letter for Mr Laurence.'
    regex = re.compile(r'Mr \w+')
    print(regex.findall(msg))
    return regex.sub('AGENT X', msg)


def replace_names_with_first_letter():
    msg = 'Mr Banker asks me to find Mr Laurence.'
    regex = re.compile(r'Mr (\w)\w*')
    # \1 means: search in the 1st group of the regex
    return regex.sub(r'AGENT \1', msg)


if __name__ == '__main__':
    print(one_word_in_a_line("Pit", "I'm working whit Pit"))
    print(one_word_in_a_line_ignore_case("Pit", "Pit is digging a pit"))
    print(start_with("Are", "Are you kidding me?"))
    print(pipe_search())
    print(start_with_multiline("If", zen))
    print(end_with("funny!", "Sometimes you are funny!"))
    print(find_digit("Arizona 479, 501, 870. California 209, 213, 650."))
    print(greedy_match(underscores_words))
    print(non_greedy_match_question_mark(underscores_words))
    print(zero_or_one_time())
    print(zero_or_more())
    print(one_or_more())
    print(find_repetition('I\'m Santa Claus OhOhOh', 'Oh', 3))
    print(find_repetition_range('You make me sing: LaLaLaLa', 'La', 3, 6))
    print(only_digit())
    print(any_chars())
    print(any_names())
    print(replace_names())
    print(replace_names_with_first_letter())
    mad_libs(text)
