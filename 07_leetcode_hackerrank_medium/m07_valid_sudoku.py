"""
================================================================================
CHALLENGE: Valid Sudoku (LeetCode 36 / Medium)
TRACK: 07_leetcode_hackerrank_medium
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid, but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
- Empty cells are represented by '.'.

INPUT FORMAT:
9 lines, each containing 9 space-separated characters (digits '1'-'9' or '.').

OUTPUT FORMAT:
Print True if valid, else False.

SAMPLE INPUT 0:
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9

SAMPLE OUTPUT 0:
True
================================================================================
"""

import sys
from collections import defaultdict
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Valid Sudoku"
POINTS = 20

TEST_CASES = [
    {
        "input": "5 3 . . 7 . . . .\n6 . . 1 9 5 . . .\n. 9 8 . . . . 6 .\n8 . . . 6 . . . 3\n4 . . 8 . 3 . . 1\n7 . . . 2 . . . 6\n. 6 . . . . 2 8 .\n. . . 4 1 9 . . 5\n. . . . 8 . . 7 9\n",
        "expected": "True",
        "hidden": False
    },
    {
        "input": "8 3 . . 7 . . . .\n6 . . 1 9 5 . . .\n. 9 8 . . . . 6 .\n8 . . . 6 . . . 3\n4 . . 8 . 3 . . 1\n7 . . . 2 . . . 6\n. 6 . . . . 2 8 .\n. . . 4 1 9 . . 5\n. . . . 8 . . 7 9\n",
        "expected": "False",
        "hidden": True
    }
]


def is_valid_sudoku(board: list) -> bool:
    # Hint: Use sets for rows, cols, and 3x3 boxes (r // 3, c // 3)
    pass


def solve():
    board = []
    for _ in range(9):
        row = input().split()
        board.append(row)
    print(is_valid_sudoku(board))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def is_valid_sudoku(board: list) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue
            box_key = (r // 3, c // 3)
            if val in rows[r] or val in cols[c] or val in boxes[box_key]:
                return False
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_key].add(val)
    return True
================================================================================
"""
