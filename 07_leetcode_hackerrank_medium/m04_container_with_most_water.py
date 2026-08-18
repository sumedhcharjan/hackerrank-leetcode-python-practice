"""
================================================================================
CHALLENGE: Container With Most Water (LeetCode 11 / Medium)
TRACK: 07_leetcode_hackerrank_medium
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
You are given an integer array `height` of length n. There are n vertical lines
drawn such that the two endpoints of the i-th line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

INPUT FORMAT:
A single line of space-separated integers representing array `height`.

OUTPUT FORMAT:
Print the maximum water area.

SAMPLE INPUT 0:
1 8 6 2 5 4 8 3 7

SAMPLE OUTPUT 0:
49

EXPLANATION 0:
The vertical lines are [1, 8, 6, 2, 5, 4, 8, 3, 7]. The max area is between index 1 (height 8)
and index 8 (height 7), area = min(8, 7) * (8 - 1) = 7 * 7 = 49.
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Container With Most Water"
POINTS = 20

TEST_CASES = [
    {"input": "1 8 6 2 5 4 8 3 7\n", "expected": "49", "hidden": False},
    {"input": "1 1\n", "expected": "1", "hidden": False},
    {"input": "4 3 2 1 4\n", "expected": "16", "hidden": True}
]


def max_area(height: list) -> int:
    # Hint: Two Pointers approach starting at both ends (left = 0, right = len(height) - 1)
    pass


def solve():
    height = list(map(int, input().split()))
    print(max_area(height))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def max_area(height: list) -> int:
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        h = min(height[left], height[right])
        w = right - left
        max_water = max(max_water, h * w)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water
================================================================================
"""
