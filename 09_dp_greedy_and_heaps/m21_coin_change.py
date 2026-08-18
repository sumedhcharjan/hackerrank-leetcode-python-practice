"""
================================================================================
CHALLENGE: Coin Change (LeetCode 322 / Medium / DP)
TRACK: 09_dp_greedy_and_heaps
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
You are given an integer array `coins` representing coins of different denominations
and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount
of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example:
Input:  coins = [1, 2, 5], amount = 11
Output: 3  (5 + 5 + 1 = 11)

INPUT FORMAT:
First line: space-separated integers for coin denominations.
Second line: integer amount.

OUTPUT FORMAT:
Print the minimum number of coins, or -1.

SAMPLE INPUT 0:
1 2 5
11

SAMPLE OUTPUT 0:
3
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Coin Change"
POINTS = 20

TEST_CASES = [
    {"input": "1 2 5\n11\n", "expected": "3", "hidden": False},
    {"input": "2\n3\n", "expected": "-1", "hidden": False},
    {"input": "1\n0\n", "expected": "0", "hidden": True}
]


def coin_change(coins: list, amount: int) -> int:
    # Hint: 1D DP table dp[i] = min coins to make amount i. dp[i] = min(dp[i], dp[i - c] + 1)
    pass


def solve():
    coins = list(map(int, input().split()))
    amount = int(input())
    print(coin_change(coins, amount))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def coin_change(coins: list, amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
================================================================================
"""
