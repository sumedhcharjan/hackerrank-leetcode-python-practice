"""
================================================================================
CHALLENGE: Text Wrap
TRACK: 03_strings_and_regex
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.

INPUT FORMAT:
The first line contains a string, S.
The second line contains the width, w.

OUTPUT FORMAT:
Print the text wrapped paragraph.

SAMPLE INPUT 0:
ABCDEFGHIJKLMNOPQRSTUVWXYZ
4

SAMPLE OUTPUT 0:
ABCD
EFGH
IJKL
MNOP
QRST
UVWX
YZ
================================================================================
"""

import sys
import textwrap
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Text Wrap"
POINTS = 10

TEST_CASES = [
    {
        "input": "ABCDEFGHIJKLMNOPQRSTUVWXYZ\n4\n",
        "expected": "ABCD\nEFGH\nIJKL\nMNOP\nQRST\nUVWX\nYZ",
        "hidden": False
    }
]


def wrap(string: str, max_width: int) -> str:
    # Hint: textwrap.fill(string, max_width)
    pass


def solve():
    string = input()
    max_width = int(input())
    result = wrap(string, max_width)
    print(result)


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def wrap(string: str, max_width: int) -> str:
    return textwrap.fill(string, max_width)
================================================================================
"""
