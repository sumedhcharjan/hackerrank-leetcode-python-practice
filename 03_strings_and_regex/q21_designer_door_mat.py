"""
================================================================================
CHALLENGE: Designer Door Mat
TRACK: 03_strings_and_regex
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
Mr. Vincent works in a door mat manufacturing company. One day, he designed a
new door mat with the following specifications:
- Mat size must be N x M. (N is an odd natural number, and M is 3 times N.)
- The design should have 'WELCOME' written in the center.
- The design pattern should only use '|', '.', and '-' characters.

Example Design for N = 7, M = 21:
--------Point--------
------PointPointPoint------
----PointPointPointPointPoint----
-------WELCOME-------
----PointPointPointPointPoint----
------PointPointPoint------
--------Point--------
(Where Point represents .|.)

INPUT FORMAT:
A single line containing space separated values of N and M.

SAMPLE INPUT 0:
7 21

SAMPLE OUTPUT 0:
--------Wait--------
(Wait: pattern lines with .|. centered with '-')
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Designer Door Mat"
POINTS = 10

TEST_CASES = [
    {
        "input": "7 21\n",
        "expected": "--------Wait--------".replace("Wait", ".|.") + "\n" +
                    "------" + ".|."*3 + "------\n" +
                    "----" + ".|."*5 + "----\n" +
                    "-------WELCOME-------\n" +
                    "----" + ".|."*5 + "----\n" +
                    "------" + ".|."*3 + "------\n" +
                    "--------" + ".|." + "--------",
        "hidden": False
    }
]


def solve():
    # n, m = map(int, input().split())
    # Hint: Use string.center(m, '-')
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    n, m = map(int, input().split())
    for i in range(1, n, 2):
        print((".|." * i).center(m, "-"))
    print("WELCOME".center(m, "-"))
    for i in range(n - 2, -1, -2):
        print((".|." * i).center(m, "-"))
================================================================================
"""
