"""
https://app.codesignal.com/tournaments/qhfBzmNJ5uGu7rxha/B

> Task
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.
The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically
and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image
'knight.jpg' to see all valid moves for a knight piece that is placed on one of the central squares.

> Example
For cell = "a1", the output should be 2.
For cell = "c2", the output should be 6.

> Input/Output
- execution time limit: 4 seconds (py3)
- input: string cell
String consisting of 2 letters - coordinates of the knight on an 8 × 8 chessboard in chess notation.
- guaranteed constraints:
cell.length = 2,
'a' ≤ cell[0] ≤ 'h',
1 ≤ cell[1] ≤ 8.
- output: integer
"""
from python_structure.code_signal_challenges.result_is_correct import is_correct


def chess_knight_moves(cell):
    def is_valid(pos):
        if 0 <= pos < 8:
            return True
        return False

    def get_x(pos):
        return ord(pos) - ord('a')

    def get_y(pos):
        return ord(pos) - ord('1')

    current_x = get_x(cell[0])
    current_y = get_y(cell[1])
    result = 0

    # (x; y)
    print("{} is at position: ({}; {})".format(cell, current_x, current_y))

    # make a range all around the knight.
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            range_x = current_x + dx
            range_y = current_y + dy
            if is_valid(range_x) and is_valid(range_y):
                # the cells around the knight which are on the chessboard
                print("({}; {})\t({}; {})".format(dx, dy, current_x + dx, current_y + dy))
                if (current_x + dx == current_x + 2 and dy == current_y + 1) or (dx == current_x + 1 and dy == current_y + 2):
                    result += 1
                    print("result: {}".format(result))
    return result


if __name__ == '__main__':
    is_correct(chess_knight_moves("a1"), 2)
    is_correct(chess_knight_moves("c2"), 6)
    is_correct(chess_knight_moves("h8"), 2)
    is_correct(chess_knight_moves("d5"), 8)
    is_correct(chess_knight_moves("a2"), 3)
    is_correct(chess_knight_moves("h7"), 3)
    is_correct(chess_knight_moves("h6"), 4)
    is_correct(chess_knight_moves("b2"), 4)
    is_correct(chess_knight_moves("f4"), 8)
