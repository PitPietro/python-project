"""
> Task
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

> Example
For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.
7 and 3 produce the largest product.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: array.integer inputArray
An array of integers containing at least two elements.
- guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
1000 ≤ inputArray[i] ≤ 1000.
- output: integer
The largest product of adjacent elements.
"""


def adjacent_elements_product(input_array):
    index_1 = 0
    index_2 = 1
    best_result = 0
    for i in range(0, int(len(input_array)/2)):
        digit_1 = input_array[index_1]
        digit_2 = input_array[index_2]

        result = digit_1 * digit_2
        print("index1: {}\tindex2: {}\td1: {}\td2: {}"
              "\nresult: {}".format(index_1, index_2, digit_1, digit_2, result))

        index_1 += 2
        index_2 += 2

        if result > best_result:
            best_result = result

    return best_result


if __name__ == '__main__':
    array = [3, 6, -2, -5, 7, 3]
    b_r = adjacent_elements_product(array)
    print("Largest product of adjacent elements:  ", b_r)
