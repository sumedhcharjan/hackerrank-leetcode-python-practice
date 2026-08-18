"""
================================================================================
CHALLENGE: Longest Substring Without Repeating Characters (LeetCode 3 / Medium)
TRACK: 07_leetcode_hackerrank_medium
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given a string `s`, find the length of the longest substring without repeating
characters.

INPUT FORMAT:
A single line containing the string `s`.

CONSTRAINTS:
0 <= s.length <= 5 * 10^4

OUTPUT FORMAT:
Print the integer length of the longest unique substring.

SAMPLE INPUT 0:
abcabcbb

SAMPLE OUTPUT 0:
3

EXPLANATION 0:
The answer is "abc", with the length of 3.
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Longest Substring Without Repeating Characters"
POINTS = 20

TEST_CASES = [
    {"input": "abcabcbb\n", "expected": "3", "hidden": False},
    {"input": "bbbbb\n", "expected": "1", "hidden": False},
    {"input": "pwwkew\n", "expected": "3", "hidden": False},
    {"input": "au\n", "expected": "2", "hidden": True}
]


def length_of_longest_substring(s: str) -> int:
    # Hint: Use Sliding Window algorithm with a hash set or dict of last seen index
    pass
    m={}
    left=int(0)
    maxlen=float("-inf")
    for i,char in enumerate(s):
        if char in m:
            left=m[char]+1
        m[char]=i
        maxlen=max(maxlen,i-left+1)
    return maxlen
    
    

def solve():
    s = input().strip()
    print(length_of_longest_substring(s))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def length_of_longest_substring(s: str) -> int:
    char_map = {}
    left = 0
    max_len = 0
    for right in range(len(s)):
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
        char_map[s[right]] = right
        max_len = max(max_len, right - left + 1)
    return max_len
================================================================================
"""
