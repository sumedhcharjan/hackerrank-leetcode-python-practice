"""
================================================================================
CHALLENGE: Arithmetic Operators
TRACK: 01_syntax_and_basics
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
The provided code stub reads two integers from STDIN, a and b. Add code to print
three lines where:
1. The first line contains the sum of the two numbers (a + b).
2. The second line contains the difference of the two numbers (first - second) (a - b).
3. The third line contains the product of the two numbers (a * b).

INPUT FORMAT:
The first line contains the first integer, a.
The second line contains the second integer, b.

CONSTRAINTS:
1 <= a <= 10^10
1 <= b <= 10^10

OUTPUT FORMAT:
Print the three lines as described above.

SAMPLE INPUT 0:
3
2

SAMPLE OUTPUT 0:
5
1
6
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Arithmetic Operators"
POINTS = 10

TEST_CASES = [
    {"input": "3\n2\n", "expected": "5\n1\n6", "hidden": False},
    {"input": "10\n5\n", "expected": "15\n5\n50", "hidden": True},
    {"input": "100\n100\n", "expected": "200\n0\n10000", "hidden": True},
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
    print(a + b)
    print(a - b)
    print(a * b)
================================================================================
"""
