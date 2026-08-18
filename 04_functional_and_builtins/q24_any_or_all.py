"""
================================================================================
CHALLENGE: Any or All
TRACK: 04_functional_and_builtins
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
You are given a space separated list of integers.
Your task is to print True if:
1. ALL integers in the list are positive (> 0), AND
2. ANY of the integers is a palindromic integer (e.g. 121, 5, 99).

Otherwise, print False.

Challenge: Solve it in 3 lines of code or less using any() and all()!

INPUT FORMAT:
The first line contains an integer N, the total number of integers.
The second line contains N space separated integers.

OUTPUT FORMAT:
Print True if all conditions are met, else False.

SAMPLE INPUT 0:
5
12 9 61 5 14

SAMPLE OUTPUT 0:
True

EXPLANATION 0:
All integers are positive. 9 and 5 are palindromic. So result is True.
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Any or All"
POINTS = 10

TEST_CASES = [
    {"input": "5\n12 9 61 5 14\n", "expected": "True", "hidden": False},
    {"input": "3\n12 34 56\n", "expected": "False", "hidden": True},
    {"input": "3\n-10 5 121\n", "expected": "False", "hidden": True}
]


def solve():
    # n = int(input())
    # numbers = input().split()
    # Hint: all(int(x) > 0 for x in numbers) and any(x == x[::-1] for x in numbers)
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    n = int(input())
    numbers = input().split()
    print(all(int(x) > 0 for x in numbers) and any(x == x[::-1] for x in numbers))
================================================================================
"""
