"""
================================================================================
CHALLENGE: 3Sum (LeetCode 15 / Medium)
TRACK: 07_leetcode_hackerrank_medium
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]`
such that i != j, i != k, and j != k, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

INPUT FORMAT:
A single line containing space-separated integers.

OUTPUT FORMAT:
Print each triplet on a new line (formatted as `nums[i] nums[j] nums[k]` sorted),
with triplets sorted lexicographically.

SAMPLE INPUT 0:
-1 0 1 2 -1 -4

SAMPLE OUTPUT 0:
-1 -1 2
-1 0 1

EXPLANATION 0:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1, -1, 2] and [-1, 0, 1].
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "3Sum"
POINTS = 20

TEST_CASES = [
    {
        "input": "-1 0 1 2 -1 -4\n",
        "expected": "-1 -1 2\n-1 0 1",
        "hidden": False
    },
    {
        "input": "0 1 1\n",
        "expected": "",
        "hidden": False
    },
    {
        "input": "0 0 0\n",
        "expected": "0 0 0",
        "hidden": True
    }
]


def three_sum(nums: list) -> list:
    # Hint: Sort array first, iterate i from 0 to len-3, use Two Pointers for rest
    pass
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return res
    

def solve():
    nums = list(map(int, input().split()))
    triplets = three_sum(nums)
    # Sort elements inside each triplet and sort triplets list
    formatted = [sorted(t) for t in triplets]
    formatted.sort()
    for t in formatted:
        print(f"{t[0]} {t[1]} {t[2]}")


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def three_sum(nums: list) -> list:
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return res
================================================================================
"""
