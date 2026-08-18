"""
================================================================================
CHALLENGE: Word Break (LeetCode 139 / Medium / DP)
TRACK: 09_dp_greedy_and_heaps
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given a string `s` and a dictionary of strings `wordDict`, return True if `s` can be
segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example:
Input:  s = "leetcode", wordDict = ["leet", "code"]
Output: True  ("leetcode" can be segmented as "leet code")

INPUT FORMAT:
First line: string `s`.
Second line: space-separated words for `wordDict`.

OUTPUT FORMAT:
Print True if segmentable, else False.

SAMPLE INPUT 0:
leetcode
leet code

SAMPLE OUTPUT 0:
True
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Word Break"
POINTS = 20

TEST_CASES = [
    {"input": "leetcode\nleet code\n", "expected": "True", "hidden": False},
    {"input": "applepenapple\napple pen\n", "expected": "True", "hidden": False},
    {"input": "catsandog\ncats dog sand and cat\n", "expected": "False", "hidden": True}
]


def word_break(s: str, word_dict: list) -> bool:
    # Hint: dp[i] represents if s[:i] can be segmented into words from word_dict
    pass


def solve():
    s = input().strip()
    word_dict = input().split()
    print(word_break(s, word_dict))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def word_break(s: str, word_dict: list) -> bool:
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True
    for i in range(len(s) - 1, -1, -1):
        for w in word_dict:
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break
    return dp[0]
================================================================================
"""
