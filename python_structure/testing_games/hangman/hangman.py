def hangman(word):
    """
    Player1: The PC
    Player2: Person guessing the word
    - 'wrong' keeps track of the incorrect guesses
    - 'stages' is a list of string representing the man, it is printed
    in the console once the program starts.
    - 'remaining_letters' is a list containing each character in the variable 'word'.
    It keeps track of which letters are left to guess.
    - 'board' is a list of string used to keep track of the game board displayed to Player2.
    It is populated with underscores for each character in the 'word' parameter.
    - 'win' keeps track of whether Player2 has won or not the game
    :param word:
    :return:
    """
    wrong = 0
    stages = ["",
              "___________     H",
              "|         |     A",
              "|         |     N",
              "|         0     G",
              "|        /|\    M",
              "|        / \    A",
              "|               N"
              ]
    remaining_letters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman \t\t - made by Pit")

    """
    The loop continues as long as 'wrong' is less than the stages' length minus one.
    So the game will continue until Player2 has guessed so many wrong letters that
    the number of strings creates the hangman.
    'char' saves the value taken as input by Player2. If the letter is guessed, look
    for the first occurrence in the 'board' list and replace it whit the 'char' value.
    The corresponding position in 'remaining_letters' is replaced by a dollar sign: it
    is easier that removing it from the list. Else, if Player2 is wrong, just implement
    the 'wrong' variable.
    """
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in remaining_letters:
            char_index = remaining_letters.index(char)
            board[char_index] = char
            remaining_letters[char_index] = '$'
        else:
            wrong += 1
        # display the board
        print((" ".join(board)))
        # print the hangman by slicing the 'stage' list
        # 'end' add one: the end slice doesn't get included in the result
        end = wrong + 1
        print("\n".join(stages[0:end]))
        # if there are not any underscores in the board, Player2 has won the game
        if "_" not in board:
            print("Win!")
            print(" ".join(board))
            win = True
            break
    # if Player2 has lost, print the full hangman
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! The word was {}.".format(word))


if __name__ == '__main__':
    hangman("Pit")
