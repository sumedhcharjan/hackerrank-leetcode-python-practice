"""
================================================================================
CHALLENGE: Combination Sum (LeetCode 39 / Backtracking)
TRACK: 08_linked_lists_trees_and_recursion
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given an array of distinct integers `candidates` and a `target` integer, return a
list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two
combinations are unique if the frequency of at least one of the chosen numbers is different.

Example:
Input:  candidates = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]

INPUT FORMAT:
First line: space-separated integers for candidates.
Second line: integer target.

OUTPUT FORMAT:
Print each combination space-separated on a new line (sorted lexicographically).

SAMPLE INPUT 0:
2 3 6 7
7

SAMPLE OUTPUT 0:
2 2 3
7
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Combination Sum"
POINTS = 20

TEST_CASES = [
    {
        "input": "2 3 6 7\n7\n",
        "expected": "2 2 3\n7",
        "hidden": False
    },
    {
        "input": "2 3 5\n8\n",
        "expected": "2 2 2 2\n2 3 3\n3 5",
        "hidden": False
    }
]


def combination_sum(candidates: list, target: int) -> list:
    # Hint: Backtracking with backtrack(index, current_sum, current_combination)
    pass


def solve():
    candidates = list(map(int, input().split()))
    target = int(input())
    res = combination_sum(candidates, target)
    
    formatted = [sorted(c) for c in res]
    formatted.sort()
    
    for c in formatted:
        print(" ".join(map(str, c)))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def combination_sum(candidates: list, target: int) -> list:
    res = []
    candidates.sort()
    
    def backtrack(start, remain, path):
        if remain == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                break
            backtrack(i, remain - candidates[i], path + [candidates[i]])
            
    backtrack(0, target, [])
    return res
================================================================================
"""
