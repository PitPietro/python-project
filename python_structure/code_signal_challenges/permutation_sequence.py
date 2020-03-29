"""
> Task
The set [1, 2, 3, ... , n] contains a total of n! unique permutations. List all the permutations
for an integer n in lexicographical order and return the kth permutation in the sequence as a string.
To build this string, concatenate decimal representations of permutation elements from left to
right without any delimiters.

> Example
For n = 3 and k = 3, the output should be "213".

The ordered list of possible permutations for 3! is:

  1) "123"
  2) "132"
  3) "213"
  4) "231"
  5) "312"
  6) "321"

The 3rd permutation in the lexicographically ordered sequence is "213".

> Input/Output
- execution time limit: 4 seconds (py3)
- input: integer n and integer k
- guaranteed constraints:
1 ≤ n ≤ 103.
1 ≤ k ≤ min(109, n!).
- output: string
A string representing the kth item in the lexicographically ordered permutation sequence for n!.

"""


def permutation(n, k):
    for i in range(0, n):
        print(i + 1)


if __name__ == '__main__':
    permutation(3, 3)
