def input_def():
    user_input = input("User input: ")

    try:
        user_input = int(user_input)
        print(user_input)
    except ValueError:
        print("Please type an integer")


if __name__ == '__main__':
    input_def()
