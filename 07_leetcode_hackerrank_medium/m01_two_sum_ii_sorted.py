"""
================================================================================
CHALLENGE: Two Sum II - Input Array Is Sorted (LeetCode 167 / Medium)
TRACK: 07_leetcode_hackerrank_medium
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing
order, find two numbers such that they add up to a specific `target` number. Let
these two numbers be `numbers[index1]` and `numbers[index2]` where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer
array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use
the same element twice. Your solution must use only O(1) extra space.

INPUT FORMAT:
First line: space-separated integers representing the array `numbers`.
Second line: integer target.

CONSTRAINTS:
2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.

OUTPUT FORMAT:
Print the 1-indexed pair of indices separated by space.

SAMPLE INPUT 0:
2 7 11 15
9

SAMPLE OUTPUT 0:
1 2

EXPLANATION 0:
The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Two Sum II - Input Array Is Sorted"
POINTS = 20

TEST_CASES = [
    {"input": "2 7 11 15\n9\n", "expected": "1 2", "hidden": False},
    {"input": "2 3 4\n6\n", "expected": "1 3", "hidden": False},
    {"input": "-1 0\n-1\n", "expected": "1 2", "hidden": True}
]


def two_sum_ii(numbers: list, target: int) -> list:
    # Hint: Use Two Pointers (left = 0, right = len(numbers) - 1)
    pass
    lo=int(0)
    hi=len(numbers)-1
    while lo<hi:
        if(numbers[hi]+numbers[lo]==target): 
            return [lo+1,hi+1]
        elif(numbers[hi]+numbers[lo]>target):
            hi=hi-1
        else:
            lo=lo+1




def solve():
    numbers = list(map(int, input().split()))
    target = int(input())
    res = two_sum_ii(numbers, target)
    print(f"{res[0]} {res[1]}")


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def two_sum_ii(numbers: list, target: int) -> list:
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
================================================================================
"""
