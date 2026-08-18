"""
================================================================================
CHALLENGE: Partition Labels (LeetCode 763 / Medium / Greedy)
TRACK: 09_dp_greedy_and_heaps
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
You are given a string `s`. We want to partition the string into as many parts as
possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order,
the resultant string should be `s`.

Return a list of integers representing the size of these parts.

Example:
Input:  s = "ababcbacadefegdehijhklij"
Output: 9 7 8  (Partitions: "ababcbaca", "defegde", "hijhklij")

INPUT FORMAT:
A single string `s`.

OUTPUT FORMAT:
Space-separated integers of partition lengths.

SAMPLE INPUT 0:
ababcbacadefegdehijhklij

SAMPLE OUTPUT 0:
9 7 8
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Partition Labels"
POINTS = 20

TEST_CASES = [
    {"input": "ababcbacadefegdehijhklij\n", "expected": "9 7 8", "hidden": False},
    {"input": "eccbbbbdec\n", "expected": "10", "hidden": False}
]


def partition_labels(s: str) -> list:
    # Hint: Store last occurrence of each character. Expand partition size until max last index reached.
    pass


def solve():
    s = input().strip()
    res = partition_labels(s)
    print(" ".join(map(str, res)))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def partition_labels(s: str) -> list:
    last_index = {char: i for i, char in enumerate(s)}
    res = []
    size = 0
    end = 0
    for i, char in enumerate(s):
        size += 1
        end = max(end, last_index[char])
        if i == end:
            res.append(size)
            size = 0
    return res
================================================================================
"""
