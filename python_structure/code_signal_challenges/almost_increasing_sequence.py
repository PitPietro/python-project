"""
> Task
Given a sequence of integers as an array, determine whether it is possible to obtain a
strictly increasing sequence by removing no more than one element from the array.
Note: sequence 'a0, a1, ..., an' is considered to be a strictly increasing if 'a0 < a1 < ... < an'.
Sequence containing only one element is also considered to be strictly increasing.

> Example
For sequence = [1, 3, 2, 1], the output should be almostIncreasingSequence(sequence) = false.
There is no one element in this array that can be removed in order to get a strictly increasing sequence.
For sequence = [1, 3, 2], the output should be almostIncreasingSequence(sequence) = true.
You can remove 3 from the array to get the strictly increasing sequence [1, 2].
Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

> Input/Output
- execution time limit: 4 seconds (py3)
- input: array.integer sequence
- guaranteed constraints:
2 ≤ sequence.length ≤ 105 & -105 ≤ sequence[i] ≤ 105.
- output] boolean
Return true if it is possible to remove one element from the array in order to
get a strictly increasing sequence, otherwise return false.
"""


def almost_increasing_sequence(sequence):
    not_inc = 0
    max_digit = sequence[0]
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1] or max_digit >= sequence[i + 1]:
            not_inc += 1
        else:
            max_digit = sequence[i + 1]
        print("max: {}\ts[{}] = {}\t s[{}] = {}\tinc = {}"
              .format(max_digit, i, sequence[i], i + 1, sequence[i+1], not_inc))

    if 0 <= not_inc <= 1:
        return True
    else:
        return False


def almost_increasing_sequence_v2(sequence):
    dropped = False
    last = prev = min(sequence) - 1
    for elements in sequence:
        if elements <= last:
            if dropped:
                return False
            else:
                dropped = True
            if elements <= prev:
                prev = last
            elif elements >= prev:
                prev = last = elements
        else:
            prev, last = last, elements
        print("prev: {}\tlast: {}\tdropped: {}\t element: {}".format(prev, last, dropped, elements))
    return True


def almost_increasing_sequence_v3(s):
    return 3 > sum((i >= j) + (i >= k) for i, j, k in zip(s, s[1:], s[2:] + [10 ** 6]))


if __name__ == '__main__':
    list_7 = [10, 1, 2, 3, 4, 5]
    b = almost_increasing_sequence(list_7)
    print(b)
    c = almost_increasing_sequence_v2(list_7)
    print(c)
    b = almost_increasing_sequence_v3(list_7)
    print(b)
