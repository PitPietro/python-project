def get_factorial_recursive(num):
    if num == 0:
        return 1
    else:
        return num * get_factorial_recursive(num - 1)


class Factorial:
    def __init__(self, n):
        self.n = n

    def print_state(self):
        print("The value of n is ", self.n)

    def get_factorial_iterative(self) -> int:
        result = 1

        for i in range(self.n):
            if i == 0 or i == 1:
                result *= 1
            else:
                result *= i

        result *= self.n
        return result


if __name__ == '__main__':
    s_main = "\n{}! is {}"
    number = 4

    fact = Factorial(number)
    fact.print_state()
    print(s_main.format(number, fact.get_factorial_iterative()))
    print(s_main.format(number, get_factorial_recursive(number)))
