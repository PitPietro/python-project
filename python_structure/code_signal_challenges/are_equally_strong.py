"""
> Task
Call two arms equally strong if the heaviest weights they each are able to
lift are equal. Call two people equally strong if their strongest arms are
equally strong (the strongest arm can be both the right and the left), and
so are their weakest arms. Given your and your friend's arms' lifting
capabilities find out if you two are equally strong.

>Example
For your_left = 10, your_right = 15, friends_left = 15, and friends_right = 10, the output should be true
For your_left = 15, your_right = 10, friends_left = 15, and friends_right = 10, the output should be true
For your_left = 15, your_right = 10, friends_left = 15, and friends_right = 9, the output should be false

> Input/Output
- execution time limit: 4 seconds (py3)
- input: integer your_left
A non-negative integer representing the heaviest weight you can lift with your left arm.
- guaranteed constraints:
0 ≤ your_left ≤ 20.

- input: integer your_right
A non-negative integer representing the heaviest weight you can lift with your right arm.
- guaranteed constraints:
0 ≤ your_right ≤ 20.

- input: integer friends_left
A non-negative integer representing the heaviest weight your friend can lift with his or her left arm.
- guaranteed constraints:
0 ≤ friends_left ≤ 20.

- input: integer friends_right
A non-negative integer representing the heaviest weight your friend can lift with his or her right arm.
- guaranteed constraints:
0 ≤ friends_right ≤ 20.

- output:
true if you and your friend are equally strong, false otherwise.
"""


def are_equally_strong(your_left, your_right, friends_left, friends_right):
    pass


if __name__ == '__main__':
    # test_n = [your_left, your_right, friends_left, friends_right]
    # true
    test_1 = [10, 15, 15, 10]
    # true
    test_2 = [15, 10, 15, 10]
    # false
    test_3 = [15, 10, 15, 9]
    # true
    test_4 = [10, 5, 5, 10]
    # false
    test_5 = [10, 15, 5, 20]
    # true
    test_6 = [10, 20, 10, 20]
    # true
    test_7 = [5, 20, 20, 5]
    # false
    test_8 = [20, 15, 5, 20]
    # true
    test_9 = [5, 10, 5, 10]
    # false
    test_10 = [1, 10, 10, 0]
    # false
    test_11 = [5, 5, 10, 10]
    # false
    test_12 = [10, 5, 10, 6]
    # true
    test_13 = [1, 1, 1, 10]
    # true
    test_14 = [0, 10, 10, 0]

    print(are_equally_strong(test_1[0], test_1[1], test_1[2], test_1[3]))
    print(are_equally_strong(test_2[0], test_2[1], test_2[2], test_2[3]))
    print(are_equally_strong(test_3[0], test_3[1], test_3[2], test_3[3]))
    print(are_equally_strong(test_4[0], test_4[1], test_4[2], test_4[3]))
    print(are_equally_strong(test_5[0], test_5[1], test_5[2], test_5[3]))
    print(are_equally_strong(test_6[0], test_6[1], test_6[2], test_6[3]))
    print(are_equally_strong(test_7[0], test_7[1], test_7[2], test_7[3]))
    print(are_equally_strong(test_8[0], test_8[1], test_8[2], test_8[3]))
    print(are_equally_strong(test_9[0], test_9[1], test_9[2], test_9[3]))
    print(are_equally_strong(test_10[0], test_10[1], test_10[2], test_10[3]))
    print(are_equally_strong(test_11[0], test_11[1], test_11[2], test_11[3]))
    print(are_equally_strong(test_12[0], test_12[1], test_12[2], test_12[3]))
    print(are_equally_strong(test_13[0], test_13[1], test_13[2], test_13[3]))
    print(are_equally_strong(test_14[0], test_14[1], test_14[2], test_14[3]))
