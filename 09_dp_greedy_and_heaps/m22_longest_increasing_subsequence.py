"""
================================================================================
CHALLENGE: Longest Increasing Subsequence (LeetCode 300 / Medium / DP)
TRACK: 09_dp_greedy_and_heaps
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

A subsequence is an array that can be derived from another array by deleting some or
no elements without changing the order of the remaining elements.

Example:
Input:  nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4  (Subsequence is [2, 3, 7, 101])

INPUT FORMAT:
Space-separated integers.

OUTPUT FORMAT:
Print the length of the longest strictly increasing subsequence.

SAMPLE INPUT 0:
10 9 2 5 3 7 101 18

SAMPLE OUTPUT 0:
4
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Longest Increasing Subsequence"
POINTS = 20

TEST_CASES = [
    {"input": "10 9 2 5 3 7 101 18\n", "expected": "4", "hidden": False},
    {"input": "0 1 0 3 2 3\n", "expected": "4", "hidden": False},
    {"input": "7 7 7 7 7\n", "expected": "1", "hidden": True}
]


def length_of_lis(nums: list) -> int:
    # Hint: dp[i] = length of LIS ending at index i. Compare with dp[j] for j < i where nums[j] < nums[i]
    pass


def solve():
    raw = input().strip()
    if not raw:
        print(0)
        return
    nums = list(map(int, raw.split()))
    print(length_of_lis(nums))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def length_of_lis(nums: list) -> int:
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
================================================================================
"""
