"""
> Task
Given a year, return the century it is in. The first century spans from the year 1 up to
and including the year 100, the second - from the year 101 up to and including the year 200, etc.

> Example
|--     input       --|-- output --|
|--    1 ≤ x ≤ 100  --|--    1   --|
|--  101 ≤ x ≤ 200  --|--    2   --|
|--       [...]     --|--   ...  --|
|-- 1701 ≤ x ≤ 1800 --|--   18   --|
|-- 1801 ≤ x ≤ 1900 --|--   19   --|

> Input/Output
- execution time limit: 4 seconds (py3)

- input: integer 'year'
A positive integer, designating the year.

- guaranteed constraints:
1 ≤ year ≤ 2005.

- output: integer
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
        print("The year {} belongs to the century n° {}".format(i, c))
        i += 100
