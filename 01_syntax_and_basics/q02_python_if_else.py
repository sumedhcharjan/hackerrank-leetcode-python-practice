"""
================================================================================
CHALLENGE: Python If-Else
TRACK: 01_syntax_and_basics
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
Given an integer, n, perform the following conditional actions:
- If n is odd, print "Weird"
- If n is even and in the inclusive range of 2 to 5, print "Not Weird"
- If n is even and in the inclusive range of 6 to 20, print "Weird"
- If n is even and greater than 20, print "Not Weird"

INPUT FORMAT:
A single line containing a positive integer, n.

CONSTRAINTS:
1 <= n <= 100

OUTPUT FORMAT:
Print "Weird" if the number is weird. Otherwise, print "Not Weird".

SAMPLE INPUT 0:
3
SAMPLE OUTPUT 0:
Weird

SAMPLE INPUT 1:
24
SAMPLE OUTPUT 1:
Not Weird
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Python If-Else"
POINTS = 10

TEST_CASES = [
    {"input": "3\n", "expected": "Weird", "hidden": False},
    {"input": "24\n", "expected": "Not Weird", "hidden": False},
    {"input": "4\n", "expected": "Not Weird", "hidden": True},
    {"input": "18\n", "expected": "Weird", "hidden": True},
    {"input": "20\n", "expected": "Weird", "hidden": True},
    {"input": "100\n", "expected": "Not Weird", "hidden": True},
]


def solve():
    # Read integer from standard input
    # n = int(input().strip())
    # Write your conditional logic below
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
================================================================================
"""
