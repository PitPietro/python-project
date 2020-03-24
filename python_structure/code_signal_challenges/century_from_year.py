"""
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

    For year = 1905, the output should be
    centuryFromYear(year) = 20;
    For year = 1700, the output should be
    centuryFromYear(year) = 17.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] integer year

    A positive integer, designating the year.

    Guaranteed constraints:
    1 ≤ year ≤ 2005.

    [output] integer
        The number of the century the year is in.

"""


def century_from_year(year):
    start = 1
    end = 100
    index = 1
    range_list = []
    for i in range(1, 22):
        range_list.append([start, end, index])
        start += 100
        end += 100
        index += 1
    # print(range_list)

    for ls in range_list:
        if ls[0] <= year <= ls[1]:
            return ls[2]


if __name__ == '__main__':
    for i in range(1, 2006):
        c = century_from_year(i)
        print(c)
        i += 100
