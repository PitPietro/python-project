import turtle


if __name__ == '__main__':
    colors = ['red', 'green', 'yellow', 'purple', 'blue', 'orange']
    turtle.bgcolor('black')

    for i in range(360):
        turtle.pencolor(colors[i % 6])
        turtle.width(int(i / 100 + 1))
        turtle.forward(i)
        turtle.left(59)
