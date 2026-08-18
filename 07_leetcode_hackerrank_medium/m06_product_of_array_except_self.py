"""
================================================================================
CHALLENGE: Product of Array Except Self (LeetCode 238 / Medium)
TRACK: 07_leetcode_hackerrank_medium
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given an integer array `nums`, return an array `answer` such that `answer[i]` is
equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and WITHOUT using the division operation.

INPUT FORMAT:
A single line containing space-separated integers.

OUTPUT FORMAT:
Print the space-separated resulting array.

SAMPLE INPUT 0:
1 2 3 4

SAMPLE OUTPUT 0:
24 12 8 6

SAMPLE INPUT 1:
-1 1 0 -3 3

SAMPLE OUTPUT 1:
0 0 9 0 0
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Product of Array Except Self"
POINTS = 20

TEST_CASES = [
    {"input": "1 2 3 4\n", "expected": "24 12 8 6", "hidden": False},
    {"input": "-1 1 0 -3 3\n", "expected": "0 0 9 0 0", "hidden": False}
]


def product_except_self(nums: list) -> list:
    # Hint: Compute prefix products left-to-right, then multiply suffix products right-to-left
    pass


def solve():
    nums = list(map(int, input().split()))
    res = product_except_self(nums)
    print(" ".join(map(str, res)))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def product_except_self(nums: list) -> list:
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res
================================================================================
"""
