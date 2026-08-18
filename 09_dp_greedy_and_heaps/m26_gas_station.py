"""
================================================================================
CHALLENGE: Gas Station (LeetCode 134 / Medium / Greedy)
TRACK: 09_dp_greedy_and_heaps
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
There are n gas stations along a circular route, where the amount of gas at the i-th
station is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from
the i-th station to its next (i + 1)-th station. You begin the journey with an empty
tank at one of the gas stations.

Given two integer arrays `gas` and `cost`, return the starting gas station's index if
you can travel around the circuit once in the clockwise direction, otherwise return -1.
If there exists a solution, it is guaranteed to be unique.

INPUT FORMAT:
First line: space-separated integers for `gas`.
Second line: space-separated integers for `cost`.

OUTPUT FORMAT:
Print starting station index or -1.

SAMPLE INPUT 0:
1 2 3 4 5
3 4 5 1 2

SAMPLE OUTPUT 0:
3
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Gas Station"
POINTS = 20

TEST_CASES = [
    {
        "input": "1 2 3 4 5\n3 4 5 1 2\n",
        "expected": "3",
        "hidden": False
    },
    {
        "input": "2 3 4\n3 4 3\n",
        "expected": "-1",
        "hidden": False
    }
]


def can_complete_circuit(gas: list, cost: list) -> int:
    # Hint: If sum(gas) < sum(cost), impossible. Otherwise greedy reset start when total < 0.
    pass


def solve():
    gas = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    print(can_complete_circuit(gas, cost))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def can_complete_circuit(gas: list, cost: list) -> int:
    if sum(gas) < sum(cost):
        return -1
    total = 0
    res = 0
    for i in range(len(gas)):
        total += (gas[i] - cost[i])
        if total < 0:
            total = 0
            res = i + 1
    return res
================================================================================
"""
