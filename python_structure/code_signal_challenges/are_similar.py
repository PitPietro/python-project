"""
> Task
Two arrays are called similar if one can be obtained from another by
swapping at most one pair of elements in one of the arrays.
Given two arrays a and b, check whether they are similar.

> Example
For a = [1, 2, 3] and b = [1, 2, 3], the output should be true.
The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be true.
We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be false.
Any swap of any two elements either in a or in b won't make a and b equal.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: array.integer a & array.integer b
a is an array of integers and b is an array of integers of the same length as a.
- guaranteed constraints:
3 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ 1000.
b.length = a.length,
1 ≤ b[i] ≤ 1000.
- output: boolean
true if a and b are similar, false otherwise.
"""
from collections import Counter as C


def are_similar(a, b):
    if a == b:
        return True
    else:
        for i in range(len(a)):
            for j in range(len(b)):
                temp_b = list(b)
                if i != j:
                    print("b[{}]: {}| b[{}]: {}".format(i, b[i], j, b[j]))
                    temp_b[j], temp_b[i] = temp_b[i], temp_b[j]
                    print("b: {}| temp_b: {}".format(b, temp_b))
                    if temp_b == a:
                        return True
        return False


def diff(list_1, list_2):
    """
    get difference of two lists
    :param list_1: list
    :param list_2: list
    :return: list
    """
    return list(set(list_1) - set(list_2))


def are_equal(a, b):
    if a == b:
        return True
    else:
        return False


def are_similar_v2(a, b):
    return C(a) == C(b) and sum(a != b for a, b in zip(a, b)) < 3


if __name__ == '__main__':
    # true
    test_1_a = [1, 2, 3]
    test_1_b = [1, 2, 3]
    # true
    test_2_a = [1, 2, 3]
    test_2_b = [2, 1, 3]
    # false
    test_3_a = [1, 2, 2]
    test_3_b = [2, 1, 1]
    # false
    test_4_a = [1, 1, 4]
    test_4_b = [1, 2, 3]
    # false
    test_5_a = [1, 2, 3]
    test_5_b = [1, 10, 2]
    # true
    test_6_a = [2, 3, 1]
    test_6_b = [1, 3, 2]
    # false
    test_7_a = [2, 3, 9]
    test_7_b = [10, 3, 2]
    # false
    test_8_a = [4, 6, 3]
    test_8_b = [3, 4, 6]
    # true
    test_9_a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
    test_9_b = [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]
    # false
    test_10_a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
    test_10_b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]

    # print(are_similar(test_1_a, test_1_b))
    print(are_similar(test_2_a, test_2_b))
    # print(are_similar(test_3_a, test_3_b))
    # print(are_similar(test_4_a, test_4_b))
    # print(are_similar(test_5_a, test_5_b))
    # print(are_similar(test_6_a, test_6_b))
    # print(are_similar(test_7_a, test_7_b))
    # print(are_similar(test_8_a, test_8_b))
    # print(are_similar(test_9_a, test_9_b))
    # print(are_similar(test_10_a, test_10_b))
