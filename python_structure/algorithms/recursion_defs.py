"""
Base Case: A condition that ends a recursive algorithm and prevent it to run continuously.
Every time a recursive function call itself, get close to the base case.
The Three Laws of Recursion:
1- A recursive algorithm must have a base case
2- A recursive algorithm must change its state and move toward the base case
3- A recursive algorithm must call itself, recursively
"""


def bottles_of_beer(bob):
    """
    Prints the lyrics of the popular song "99 bottles of beer on the wall"
    :param bob: number of beer
    :return: lyrics
    """
    if bob < 1:
        print("""No more bottles of beer on the wall. No more bottles of beer.""")
        return
    tmp = bob
    bob -= 1

    print("""{} bottles of beer on the wall. {} bottles of beer.
    Take on down, pass it around, {} bottles of beer on the wall.""".format(tmp, tmp, bob))
    bottles_of_beer(bob)


def print_to_zero(n):
    """
    Prints all the number from 'n' to zero
    :param n:
    :return: nothing
    """
    if n < 0:
        return
    print(n)
    print_to_zero(n - 1)


def sum_all(n):
    """
    Sum all the number from 'n' to one
    :param n: a number
    :return: 1 + 2 + ... + n
    """
    if n > 1:
        return n + sum_all(n - 1)
    else:
        return n


def multiply_all(n):
    """
    Multiply all the number from 'n' to one. The if condition takes as
    reference 2 since 1 is the identity element for multiplication.
    :param n: a number
    :return: 1 * 2 * ... * n
    """
    if n > 2:
        return n * sum_all(n - 1)
    else:
        return n


if __name__ == '__main__':
    bottles_of_beer(5)
    print("\n")
    print_to_zero(5)
    print("\n")
    print(sum_all(3))
    print(multiply_all(4))
