"""
For functions that returns a boolean value.
1° parameter: the function result
2° parameter: the expected result
"""


def is_correct(def_res, result):
    if def_res == result:
        print("Correct")
    else:
        print("INCORRECT")