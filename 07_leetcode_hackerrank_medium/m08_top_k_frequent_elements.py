"""
================================================================================
CHALLENGE: Top K Frequent Elements (LeetCode 347 / Medium)
TRACK: 07_leetcode_hackerrank_medium
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given an integer array `nums` and an integer `k`, return the `k` most frequent
elements. You may return the answer in any order.

Your algorithm's time complexity must be better than O(n log n), where n is the
array's size.

INPUT FORMAT:
First line: space-separated integers representing array `nums`.
Second line: integer `k`.

OUTPUT FORMAT:
Print the `k` most frequent elements space-separated (sorted in ascending order for output comparison).

SAMPLE INPUT 0:
1 1 1 2 2 3
2

SAMPLE OUTPUT 0:
1 2

EXPLANATION 0:
1 occurs 3 times, 2 occurs 2 times, 3 occurs 1 time. The 2 most frequent elements are 1 and 2.
================================================================================
"""

import sys
from collections import Counter
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Top K Frequent Elements"
POINTS = 20

TEST_CASES = [
    {"input": "1 1 1 2 2 3\n2\n", "expected": "1 2", "hidden": False},
    {"input": "1\n1\n", "expected": "1", "hidden": False},
    {"input": "4 4 4 6 6 7 8 8 8 8\n2\n", "expected": "4 8", "hidden": True}
]


def top_k_frequent(nums: list, k: int) -> list:
    # Hint: Use collections.Counter(nums).most_common(k)
    pass


def solve():
    nums = list(map(int, input().split()))
    k = int(input())
    res = top_k_frequent(nums, k)
    print(" ".join(map(str, sorted(res))))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def top_k_frequent(nums: list, k: int) -> list:
    count = Counter(nums)
    return [item[0] for item in count.most_common(k)]
================================================================================
"""
