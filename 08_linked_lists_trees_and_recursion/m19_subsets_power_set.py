"""
================================================================================
CHALLENGE: Subsets / Power Set (LeetCode 78 / Backtracking)
TRACK: 08_linked_lists_trees_and_recursion
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given an integer array `nums` of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example:
Input:  nums = [1, 2, 3]
Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

INPUT FORMAT:
Space-separated integers.

OUTPUT FORMAT:
Print each subset space-separated on a new line (subsets sorted by length/elements for comparison).

SAMPLE INPUT 0:
1 2 3

SAMPLE OUTPUT 0:
[]
1
2
3
1 2
1 3
2 3
1 2 3
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Subsets / Power Set"
POINTS = 20

TEST_CASES = [
    {
        "input": "1 2 3\n",
        "expected": "[]\n1\n2\n3\n1 2\n1 3\n2 3\n1 2 3",
        "hidden": False
    },
    {
        "input": "0\n",
        "expected": "[]\n0",
        "hidden": False
    }
]


def subsets(nums: list) -> list:
    # Hint: Use backtracking recursion: backtrack(index, current_path)
    pass
    ans=[]
    def help(idx:int, combi:list) -> None:
        if(idx>=len(nums)):
            ans.append(combi.copy())
            return

        help(idx+1,combi)
        combi.extend([nums[idx]])
        help(idx+1,combi)
        combi.pop()
        return
    help(0,[])
    return ans



def solve():
    raw = input().strip()
    if not raw:
        print("[]")
        return
    nums = list(map(int, raw.split()))
    res = subsets(nums)
    
    # Sort elements inside each subset, and sort subsets by length and content
    formatted = [sorted(s) for s in res]
    formatted.sort(key=lambda s: (len(s), s))
    
    for s in formatted:
        if not s:
            print("[]")
        else:
            print(" ".join(map(str, s)))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def subsets(nums: list) -> list:
    res = []
    def backtrack(i, path):
        if i == len(nums):
            res.append(path[:])
            return
        # Include nums[i]
        backtrack(i + 1, path + [nums[i]])
        # Exclude nums[i]
        backtrack(i + 1, path)
    backtrack(0, [])
    return res
================================================================================
"""
