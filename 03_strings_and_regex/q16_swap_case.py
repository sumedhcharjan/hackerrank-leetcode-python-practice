"""
================================================================================
CHALLENGE: sWAP cASE
TRACK: 03_strings_and_regex
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
You are given a string and your task is to swap cases. In other words, convert
all lowercase letters to uppercase letters and vice versa.

Example:
WWW.HackerRank.com → www.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

INPUT FORMAT:
A single line containing a string s.

OUTPUT FORMAT:
Print the modified string s.

SAMPLE INPUT 0:
HackerRank.com presents "Pythonist 2".

SAMPLE OUTPUT 0:
hACKERrANK.COM PRESENTS "pYTHONIST 2".
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "sWAP cASE"
POINTS = 10

TEST_CASES = [
    {
        "input": "HackerRank.com presents \"Pythonist 2\".\n",
        "expected": "hACKERrANK.COM PRESENTS \"pYTHONIST 2\".",
        "hidden": False
    }
]


def swap_case(s: str) -> str:
    # Write your swapcase implementation or use s.swapcase()
    pass


def solve():
    s = input()
    print(swap_case(s))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def swap_case(s: str) -> str:
    return s.swapcase()
================================================================================
"""
