"""
================================================================================
CHALLENGE: Kth Largest Element in an Array (LeetCode 215 / Medium / Heap)
TRACK: 09_dp_greedy_and_heaps
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given an integer array `nums` and an integer `k`, return the k-th largest element
in the array.

Note that it is the k-th largest element in the sorted order, not the k-th distinct element.

Can you solve it without sorting the entire array in O(n log k) time using a Min-Heap?

Example:
Input:  nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5

INPUT FORMAT:
First line: space-separated integers for array `nums`.
Second line: integer `k`.

OUTPUT FORMAT:
Print the k-th largest element.

SAMPLE INPUT 0:
3 2 1 5 6 4
2

SAMPLE OUTPUT 0:
5
================================================================================
"""

import sys
import heapq
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Kth Largest Element in an Array"
POINTS = 20

TEST_CASES = [
    {"input": "3 2 1 5 6 4\n2\n", "expected": "5", "hidden": False},
    {"input": "3 2 3 1 2 4 5 5 6\n4\n", "expected": "4", "hidden": False}
]


def find_kth_largest(nums: list, k: int) -> int:
    # Hint: Maintain a min-heap of size k using heapq.heappush & heapq.heappop
    pass


def solve():
    nums = list(map(int, input().split()))
    k = int(input())
    print(find_kth_largest(nums, k))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def find_kth_largest(nums: list, k: int) -> int:
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]
================================================================================
"""
