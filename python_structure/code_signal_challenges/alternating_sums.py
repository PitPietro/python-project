"""
> Task
Several people are standing in a row and need to be divided into two teams.
The first person goes into team 1, the second goes into team 2, the third
goes into team 1 again, the fourth into team 2, and so on.
You are given an array of positive integers - the weights of the people.
Return an array of two integers, where the first element is the total weight
of team 1, and the second element is the total weight of team 2 after the division is complete.

> Example
For a = [50, 60, 60, 45, 70], the output should be [180, 105].

> Input/Output
- execution time limit: 4 seconds (py3)
- input: array.integer a
- guaranteed constraints:
1 ≤ a.length ≤ 105,
45 ≤ a[i] ≤ 100.
- output: array.integer
"""


def alternating_sums(a):
    team_1 = []
    team_2 = []
    for i in range(len(a)):
        index = i + 1
        print("a[{}] = {}".format(index, a[i]))
        if index % 2 != 0:
            team_1.append(a[i])
            print("team 1: {}".format(team_1))
        elif index % 2 == 0:
            team_2.append(a[i])
            print("team 2: {}".format(team_2))
    print("\n\nteam 1: {}\nteam 2: {}".format(team_1, team_2))
    element_1 = sum(team_1)
    element_2 = sum(team_2)
    print("\n\nsum 1: {}\nsum 2: {}".format(element_1, element_2))
    return [sum(team_1), sum(team_2)]


if __name__ == '__main__':
    test_1 = [50, 60, 60, 45, 70]
    print(alternating_sums(test_1))
