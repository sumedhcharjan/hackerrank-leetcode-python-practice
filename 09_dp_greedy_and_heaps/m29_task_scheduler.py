"""
================================================================================
CHALLENGE: Task Scheduler (LeetCode 621 / Medium / Heap & Greedy)
TRACK: 09_dp_greedy_and_heaps
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given a characters array `tasks`, representing the tasks a CPU needs to do, where
each letter represents a different task. Tasks could be done in any order. Each task
is done in one unit of time. For each unit of time, the CPU could have done one task
or just be idle.

However, there is a non-negative integer `n` that represents the cooldown period between
two same tasks (same letter in tasks), that is that there must be at least `n` units of
time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example:
Input:  tasks = ["A", "A", "A", "B", "B", "B"], n = 2
Output: 8  (Sequence: A -> B -> idle -> A -> B -> idle -> A -> B)

INPUT FORMAT:
First line: space-separated task character names.
Second line: integer cooldown `n`.

OUTPUT FORMAT:
Print the minimum time units required.

SAMPLE INPUT 0:
A A A B B B
2

SAMPLE OUTPUT 0:
8
================================================================================
"""

import sys
from collections import Counter
import heapq
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Task Scheduler"
POINTS = 20

TEST_CASES = [
    {"input": "A A A B B B\n2\n", "expected": "8", "hidden": False},
    {"input": "A A A B B B\n0\n", "expected": "6", "hidden": False}
]


def least_interval(tasks: list, n: int) -> int:
    # Hint: Count task frequencies. Max frequency determines idle slots needed.
    pass


def solve():
    tasks = input().split()
    n = int(input())
    print(least_interval(tasks, n))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def least_interval(tasks: list, n: int) -> int:
    counts = Counter(tasks)
    max_freq = max(counts.values())
    max_freq_count = sum(1 for count in counts.values() if count == max_freq)
    
    empty_slots = (max_freq - 1) * (n + 1) + max_freq_count
    return max(len(tasks), empty_slots)
================================================================================
"""
