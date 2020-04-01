"""
> Task
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky
if the sum of the first half of the digits is equal to the sum of the second half. Given a ticket
number n, determine if it's lucky or not.

> Example
For n = 1230, the output should be true
For n = 239017, the output should be false.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: integer n
A ticket number represented as a positive integer with an even number of digits.
- guaranteed constraints:
10 ≤ n < 106.
- output: boolean
true if n is a lucky ticket number, false otherwise.
"""


def is_lucky(n):
    str_n = str(n)
    half = len(str_n) // 2
    first_sum = 0
    second_sum = 0
    print("half: {}".format(half))
    for i in range(len(str_n)):
        print(str_n[i])

    for i in range(half):
        first_sum += int(str_n[i])
        print("1st half sum: {}\tsum: {}".format(i, first_sum))

    for j in range(half, len(str_n)):
        second_sum += int(str_n[j])
        print("2nd half sum: {}\tsum: {}".format(j, second_sum))


if __name__ == '__main__':
    print(is_lucky(1230))
