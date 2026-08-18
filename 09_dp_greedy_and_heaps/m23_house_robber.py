"""
================================================================================
CHALLENGE: House Robber (LeetCode 198 / Medium / DP)
TRACK: 09_dp_greedy_and_heaps
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
You are a professional robber planning to rob houses along a street. Each house has a
certain amount of money stashed, the only constraint stopping you from robbing each
of them is that adjacent houses have security systems connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return
the maximum amount of money you can rob tonight without alerting the police.

Example:
Input:  nums = [1, 2, 3, 1]
Output: 4  (Rob house 1 (money = 1) and rob house 3 (money = 3). Total = 1 + 3 = 4)

INPUT FORMAT:
Space-separated integers.

OUTPUT FORMAT:
Print maximum money robbed.

SAMPLE INPUT 0:
1 2 3 1

SAMPLE OUTPUT 0:
4
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "House Robber"
POINTS = 20

TEST_CASES = [
    {"input": "1 2 3 1\n", "expected": "4", "hidden": False},
    {"input": "2 7 9 3 1\n", "expected": "12", "hidden": False},
    {"input": "2 1 1 2\n", "expected": "4", "hidden": True}
]


def rob(nums: list) -> int:
    # Hint: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    pass


def solve():
    raw = input().strip()
    if not raw:
        print(0)
        return
    nums = list(map(int, raw.split()))
    print(rob(nums))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def rob(nums: list) -> int:
    rob1, rob2 = 0, 0
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2
================================================================================
"""
