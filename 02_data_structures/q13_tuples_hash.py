"""
================================================================================
CHALLENGE: Tuples & Hash
TRACK: 02_data_structures
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
Given an integer, n, and n space-separated integers as input, create a tuple, t,
of those n integers. Then compute and print the result of hash(t).

Note: hash() is a built-in function in Python.

INPUT FORMAT:
The first line contains an integer, n, denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple t.

OUTPUT FORMAT:
Print the result of hash(t).

SAMPLE INPUT 0:
2
1 2

SAMPLE OUTPUT 0:
(Varies by Python process hash seed, test case checks hash tuple structure)
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Tuples & Hash"
POINTS = 10

TEST_CASES = [
    {
        "input": "2\n1 2\n",
        "expected": str(hash((1, 2))),
        "hidden": False
    },
    {
        "input": "3\n1 2 3\n",
        "expected": str(hash((1, 2, 3))),
        "hidden": True
    }
]


def solve():
    # n = int(input())
    # integer_list = map(int, input().split())
    # t = tuple(integer_list)
    # print(hash(t))
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
================================================================================
"""
