def get_factorial_recursive(num):
    return num * get_factorial_recursive(num - 1) if num else 1


class Factorial:
    def __init__(self, n):
        self.n = n

    def print_state(self):
        print("The value of n is ", self.n)

    def get_factorial_iterative(self) -> int:
        result = 1

        for i in range(self.n + 1):
            result *= max(1, i)

        return result


if __name__ == '__main__':
    s_main = "\n{}! is {}"
    number = 4

    fact = Factorial(number)
    fact.print_state()
    print(s_main.format(number, fact.get_factorial_iterative()))
    print(s_main.format(number, get_factorial_recursive(number)))
