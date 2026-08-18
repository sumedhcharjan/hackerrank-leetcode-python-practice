"""
================================================================================
CHALLENGE: Loops
TRACK: 01_syntax_and_basics
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
The provided code stub reads an integer, n, from STDIN. For all non-negative
integers i < n, print i^2.

INPUT FORMAT:
The first and only line contains the integer, n.

CONSTRAINTS:
1 <= n <= 20

OUTPUT FORMAT:
Print n lines, one corresponding to each i (0 <= i < n), containing the value i^2.

SAMPLE INPUT 0:
5

SAMPLE OUTPUT 0:
0
1
4
9
16
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Loops"
POINTS = 10

TEST_CASES = [
    {"input": "5\n", "expected": "0\n1\n4\n9\n16", "hidden": False},
    {"input": "3\n", "expected": "0\n1\n4", "hidden": True},
    {"input": "1\n", "expected": "0", "hidden": True},
]


def solve():
    # n = int(input())
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    n = int(input())
    for i in range(n):
        print(i ** 2)
================================================================================
"""
