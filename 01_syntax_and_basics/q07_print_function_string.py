"""
================================================================================
CHALLENGE: Print Function
TRACK: 01_syntax_and_basics
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
The included code stub will read an integer, n, from STDIN.

Without using any string methods, try to print the following:
123...n

Note that "..." represents the consecutive values in between.

Example:
n = 5
Print the string 12345.

INPUT FORMAT:
The first line contains an integer n.

CONSTRAINTS:
1 <= n <= 150

OUTPUT FORMAT:
Print the list of integers from 1 through n as a string, without spaces.

SAMPLE INPUT 0:
3

SAMPLE OUTPUT 0:
123
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Print Function"
POINTS = 10

TEST_CASES = [
    {"input": "3\n", "expected": "123", "hidden": False},
    {"input": "5\n", "expected": "12345", "hidden": True},
    {"input": "10\n", "expected": "12345678910", "hidden": True},
]


def solve():
    # n = int(input())
    # Hint: Use print(*objects, sep='', end='')
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    n = int(input())
    for i in range(1, n + 1):
        print(i, end="")
================================================================================
"""
