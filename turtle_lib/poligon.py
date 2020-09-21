import turtle


def polygon():
    polygon_ = turtle.Turtle()
    for i in range(6):
        polygon_.forward(100)
        polygon_.right(300)
    turtle.done()


if __name__ == '__main__':
    polygon()
