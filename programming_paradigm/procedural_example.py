authors = []


def collect_authors():
    while True:
        answer = input("Type an author: ")
        if answer == "x" or answer == "X":
            break
        authors.append(answer)
        print(authors)


if __name__ == '__main__':
    print("Press X to exit\n")
    collect_authors()
