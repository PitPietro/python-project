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
import sys


def adjacent_elements_product(input_array):
    index_1 = 0
    index_2 = 1
    best_result = sys.maxsize * -1
    for i in range(0, int(len(input_array) - 1)):
        digit_1 = input_array[index_1]
        digit_2 = input_array[index_2]

        result = digit_1 * digit_2
        print("index1: {}\tindex2: {}\t--|--\td1: {}\td2: {}"
              "\nresult: {}".format(index_1, index_2, digit_1, digit_2, result))

        index_1 += 1
        index_2 += 1

        if result > best_result:
            best_result = result

    print("{} ---> {}\n".format(input_array,  best_result))
    # return best_result


if __name__ == '__main__':
    list_1 = [3, 6, -2, -5, 7, 3]
    list_2 = [-1, -2]
    list_3 = [5, 1, 2, 3, 1, 4]
    list_4 = [5, 6, -4, 2, 3, 2, -23]
    list_5 = [1, 2, 3, 0]
    list_6 = [9, 5, 10, 2, 24, -1, -48]
    list_7 = [-23, 4, -3, 8, -12]

    adjacent_elements_product(list_1)
    adjacent_elements_product(list_2)
    adjacent_elements_product(list_3)
    adjacent_elements_product(list_4)
    adjacent_elements_product(list_5)
    adjacent_elements_product(list_6)
    adjacent_elements_product(list_7)
