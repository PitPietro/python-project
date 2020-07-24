import webbrowser


def open_duckduckgo(keyword):
    keyword = keyword.replace(' ', '+')
    webbrowser.open('https://duckduckgo.com/?q={}&t=hk&ia=web'.format(keyword))


if __name__ == '__main__':
    # TODO: Make it a script where you pass the search string as argument.
    open_duckduckgo('hello world')
