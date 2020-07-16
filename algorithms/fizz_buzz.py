"""
Print the number from 1 to 100.
If the number is a multiple of 3, print "Fizz".
If it is a multiple of 5, print "Buzz" and if it
is multiple of both 3 and 5, print "FizzBuzz".
"""


def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    fizz_buzz()