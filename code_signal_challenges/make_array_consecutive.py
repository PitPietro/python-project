"""
> Task
Mark got statues of different sizes as a present from CodeMaster for his birthday, each statue having
an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest
to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional
statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

> Example
For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.
Mark needs statues of sizes 4, 5 and 7.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: array.integer statues
An array of distinct non-negative integers.
- guaranteed constraints:
1 ≤ statues.length ≤ 10,
0 ≤ statues[i] ≤ 20.
- output: integer
The minimal number of statues that need to be added to existing statues such that it contains every integer
size from an interval [L, R] (for some L, R) and no other sizes.
"""
from algorithms.sorting_algorithms.bubble_sort import bubble_sort


def make_array_consecutive(int_list):
    bubble_sort(int_list)
    elements = 0
    for i in range(len(int_list) - 1):
        first = int_list[i]
        second = int_list[i + 1]
        if first < second:
            for j in range(first, second - 1):
                elements += 1
    return elements


def make_array_consecutive_v2(int_list):
    return max(int_list) - min(int_list) - len(int_list) + 1


def make_array_consecutive_v3(int_list):
    return sum([1 for i in range(min(int_list), max(int_list)) if i not in int_list])


if __name__ == '__main__':
    statues = [6, 2, 3, 8]
    result_1 = make_array_consecutive(statues)
    result_2 = make_array_consecutive_v2(statues)
    result_3 = make_array_consecutive_v3(statues)

    print(result_1)
    print(result_2)
    print(result_3)
