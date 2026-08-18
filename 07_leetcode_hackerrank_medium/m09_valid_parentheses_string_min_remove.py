"""
================================================================================
CHALLENGE: Minimum Add to Make Parentheses Valid (LeetCode 921 / Medium)
TRACK: 07_leetcode_hackerrank_medium
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
A parentheses string is valid if and only if:
- It is the empty string,
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis
at any position of the string.
- For example, if s = "()))", you can insert an open parenthesis at the beginning
  to make it "(()))" or a closing parenthesis to make it "()()))".

Return the minimum number of moves required to make `s` valid.

INPUT FORMAT:
A single string `s` containing only '(' and ')'.

OUTPUT FORMAT:
Print the minimum number of additions needed.

SAMPLE INPUT 0:
())

SAMPLE OUTPUT 0:
1

SAMPLE INPUT 1:
(((

SAMPLE OUTPUT 1:
3
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Minimum Add to Make Parentheses Valid"
POINTS = 20

TEST_CASES = [
    {"input": "())\n", "expected": "1", "hidden": False},
    {"input": "(((\n", "expected": "3", "hidden": False},
    {"input": "()\n", "expected": "0", "hidden": True},
    {"input": "()))((\n", "expected": "4", "hidden": True}
]


def min_add_to_make_valid(s: str) -> int:
    # Hint: Keep track of open count balance and needed closing/opening brackets
    pass


def solve():
    s = input().strip()
    print(min_add_to_make_valid(s))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def min_add_to_make_valid(s: str) -> int:
    open_needed = 0
    close_needed = 0
    for char in s:
        if char == '(':
            close_needed += 1
        elif char == ')':
            if close_needed > 0:
                close_needed -= 1
            else:
                open_needed += 1
    return open_needed + close_needed
================================================================================
"""
