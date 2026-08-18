"""
================================================================================
CHALLENGE: K Closest Points to Origin (LeetCode 973 / Medium / Heap)
TRACK: 09_dp_greedy_and_heaps
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given an array of `points` where `points[i] = [x_i, y_i]` represents a point on the X-Y
plane and an integer `k`, return the `k` closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance:
    sqrt((x1 - x2)^2 + (y1 - y2)^2)

You may return the answer in any order. The answer is guaranteed to be unique
(except for the order that it is in).

INPUT FORMAT:
First line: integer N (number of points).
Next N lines: space-separated integers `x y` for each point.
Last line: integer `k`.

OUTPUT FORMAT:
Print the k closest points, sorted by x coordinate then y coordinate for test output comparison.

SAMPLE INPUT 0:
2
1 3
-2 2
1

SAMPLE OUTPUT 0:
-2 2

EXPLANATION 0:
Distance of (1, 3) is sqrt(1^2 + 3^2) = sqrt(10).
Distance of (-2, 2) is sqrt((-2)^2 + 2^2) = sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
================================================================================
"""

import sys
import heapq
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "K Closest Points to Origin"
POINTS = 20

TEST_CASES = [
    {
        "input": "2\n1 3\n-2 2\n1\n",
        "expected": "-2 2",
        "hidden": False
    },
    {
        "input": "3\n3 3\n5 -1\n-2 4\n2\n",
        "expected": "-2 4\n3 3",
        "hidden": False
    }
]


def k_closest(points: list, k: int) -> list:
    # Hint: Use max-heap of size k storing (-dist, x, y) or heapq.nsmallest
    pass


def solve():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append([x, y])
    k = int(input())
    
    res = k_closest(points, k)
    res.sort(key=lambda p: (p[0], p[1]))
    for p in res:
        print(f"{p[0]} {p[1]}")


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def k_closest(points: list, k: int) -> list:
    max_heap = []
    for x, y in points:
        dist = -(x*x + y*y)
        if len(max_heap) < k:
            heapq.heappush(max_heap, (dist, x, y))
        else:
            heapq.heappushpop(max_heap, (dist, x, y))
    return [[x, y] for dist, x, y in max_heap]
================================================================================
"""
