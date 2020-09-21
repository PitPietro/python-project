import turtle
import time


def test():
    pen = turtle.Turtle()
    pen.home()
    for i in range(400):
        pen.setx(i)
        pen.seth(i)
        x_value = pen.xcor()
        y_value = pen.ycor()
        angle = pen.heading()
        print('i = {}°\ta = {}°\tx = {} y = {}'.format(i, angle, x_value, y_value))
        time.sleep(0.001)

    # pen.down()
    # pen.goto(0.5, 0.5)
    # pen.forward(100)
    # pen.left(90)
    # pen.forward(100)
    turtle.done()


if __name__ == '__main__':
    test()
