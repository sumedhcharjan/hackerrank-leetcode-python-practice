"""
================================================================================
CHALLENGE: itertools.product()
TRACK: 06_algorithms_and_math
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same tuples as ((x,y) for x in A for y in B).

Task:
You are given two lists A and B. Your task is to compute their cartesian product A x B.

INPUT FORMAT:
The first line contains space separated elements of list A.
The second line contains space separated elements of list B.

OUTPUT FORMAT:
Output the space separated tuples of the cartesian product.

SAMPLE INPUT 0:
1 2
3 4

SAMPLE OUTPUT 0:
(1, 3) (1, 4) (2, 3) (2, 4)
================================================================================
"""

import sys
from itertools import product
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "itertools.product()"
POINTS = 10

TEST_CASES = [
    {
        "input": "1 2\n3 4\n",
        "expected": "(1, 3) (1, 4) (2, 3) (2, 4)",
        "hidden": False
    }
]


def solve():
    # a = list(map(int, input().split()))
    # b = list(map(int, input().split()))
    # Hint: print(*product(a, b))
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    from itertools import product
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(*product(a, b))
================================================================================
"""
