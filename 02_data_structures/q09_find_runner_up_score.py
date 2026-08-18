"""
================================================================================
CHALLENGE: Find the Runner-Up Score!
TRACK: 02_data_structures
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
Given the participants' score sheet for your University Sports Day, you are
required to find the runner-up score. You are given n scores. Store them in a
list and find the score of the runner-up (2nd highest score).

INPUT FORMAT:
The first line contains n.
The second line contains an array A[] of n integers separated by a space.

CONSTRAINTS:
2 <= n <= 10
-100 <= A[i] <= 100

OUTPUT FORMAT:
Print the runner-up score.

SAMPLE INPUT 0:
5
2 3 6 6 5

SAMPLE OUTPUT 0:
5

EXPLANATION 0:
Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum score is 5.
Hence, we print 5 as the runner-up score.
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Find the Runner-Up Score!"
POINTS = 10

TEST_CASES = [
    {"input": "5\n2 3 6 6 5\n", "expected": "5", "hidden": False},
    {"input": "4\n-10 -10 -5 -1\n", "expected": "-5", "hidden": True},
    {"input": "5\n5 7 7 9 9\n", "expected": "7", "hidden": True},
]


def solve():
    # n = int(input())
    # arr = map(int, input().split())
    # Hint: Convert to set to remove duplicates, or sort and find 2nd max
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    unique_scores = sorted(list(set(arr)), reverse=True)
    print(unique_scores[1])
================================================================================
"""
