"""
================================================================================
CHALLENGE: Jump Game (LeetCode 55 / Medium / Greedy)
TRACK: 09_dp_greedy_and_heaps
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
You are given an integer array `nums`. You are initially positioned at the array's
first index, and each element in the array represents your maximum jump length at that position.

Return True if you can reach the last index, or False otherwise.

Example:
Input:  nums = [2, 3, 1, 1, 4]
Output: True  (Jump 1 step from index 0 to 1, then 3 steps to the last index)

INPUT FORMAT:
Space-separated integers.

OUTPUT FORMAT:
Print True if reachable, else False.

SAMPLE INPUT 0:
2 3 1 1 4

SAMPLE OUTPUT 0:
True

SAMPLE INPUT 1:
3 2 1 0 4

SAMPLE OUTPUT 1:
False
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Jump Game"
POINTS = 20

TEST_CASES = [
    {"input": "2 3 1 1 4\n", "expected": "True", "hidden": False},
    {"input": "3 2 1 0 4\n", "expected": "False", "hidden": False},
    {"input": "0\n", "expected": "True", "hidden": True}
]


def can_jump(nums: list) -> bool:
    # Hint: Greedy approach iterating backward moving the target goal post
    pass


def solve():
    raw = input().strip()
    if not raw:
        print(True)
        return
    nums = list(map(int, raw.split()))
    print(can_jump(nums))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def can_jump(nums: list) -> bool:
    goal = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0
================================================================================
"""
