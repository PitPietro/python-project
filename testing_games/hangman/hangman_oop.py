class Hangman:
    def __init__(self, word):
        self.word = word

    def play_game(self):
        self.word = self.word.upper()
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
        remaining_letters = list(self.word)
        board = ["_"] * len(self.word)
        win = False
        print("Welcome to Hangman \t\t - made by Pit")
        while wrong < len(stages) - 1:
            print("\n")
            msg = "Guess a letter: "
            char = input(msg).upper()
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
            print("\n".join(stages))
            print("|________________\nYou lose! The word was {}.".format(self.word))
