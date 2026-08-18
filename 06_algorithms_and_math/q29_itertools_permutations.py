"""
================================================================================
CHALLENGE: itertools.permutations()
TRACK: 06_algorithms_and_math
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
This tool returns successive r length permutations of elements in an iterable.
If r is not specified or is None, then r defaults to the length of the iterable and
all possible full-length permutations are generated.

Task:
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

INPUT FORMAT:
A single line containing the space separated string S and the integer value k.

CONSTRAINTS:
0 < k <= len(S)
The string contains only UPPERCASE characters.

OUTPUT FORMAT:
Print the permutations of the string S on separate lines.

SAMPLE INPUT 0:
HACK 2

SAMPLE OUTPUT 0:
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
================================================================================
"""

import sys
from itertools import permutations
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "itertools.permutations()"
POINTS = 10

TEST_CASES = [
    {
        "input": "HACK 2\n",
        "expected": "AC\nAH\nAK\nCA\nCH\nCK\nHA\nHC\nHK\nKA\nKC\nKH",
        "hidden": False
    }
]


def solve():
    # s, k = input().split()
    # k = int(k)
    # Hint: Sort string s first! sorted(s)
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    from itertools import permutations
    s, k = input().split()
    for p in permutations(sorted(s), int(k)):
        print("".join(p))
================================================================================
"""
