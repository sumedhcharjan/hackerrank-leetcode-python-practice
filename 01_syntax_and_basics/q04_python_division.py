"""
================================================================================
CHALLENGE: Python: Division
TRACK: 01_syntax_and_basics
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
The provided code stub reads two integers, a and b, from STDIN.
Add logic to print two lines:
1. The first line should contain integer division, a // b.
2. The second line should contain float division, a / b.

No rounding or formatting is necessary.

INPUT FORMAT:
The first line contains the first integer, a.
The second line contains the second integer, b.

OUTPUT FORMAT:
Print the two lines as described above.

SAMPLE INPUT 0:
4
3

SAMPLE OUTPUT 0:
1
1.3333333333333333
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Python: Division"
POINTS = 10

TEST_CASES = [
    {"input": "4\n3\n", "expected": "1\n1.3333333333333333", "hidden": False},
    {"input": "10\n2\n", "expected": "5\n5.0", "hidden": True},
    {"input": "7\n2\n", "expected": "3\n3.5", "hidden": True},
]


def solve():
    # a = int(input())
    # b = int(input())
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)
================================================================================
"""
