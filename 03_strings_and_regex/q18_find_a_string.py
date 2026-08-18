"""
================================================================================
CHALLENGE: Find a string
TRACK: 03_strings_and_regex
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
In this challenge, the user enters a string and a substring. You have to print the
number of times that the substring occurs in the given string. String traversal
will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.
Overlapping substrings ARE counted!
Example: 'CDC' in 'ABCDCDC' occurs 2 times (indices 2..4 and 4..6).

INPUT FORMAT:
The first line of input contains the original string.
The second line contains the substring.

OUTPUT FORMAT:
Output the integer number indicating the total number of occurrences of the substring.

SAMPLE INPUT 0:
ABCDCDC
CDC

SAMPLE OUTPUT 0:
2
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Find a string"
POINTS = 10

TEST_CASES = [
    {"input": "ABCDCDC\nCDC\n", "expected": "2", "hidden": False},
    {"input": "AAAAA\nAA\n", "expected": "4", "hidden": True}
]


def count_substring(string: str, sub_string: str) -> int:
    # Note: str.count() does NOT count overlapping substrings by default!
    pass


def solve():
    string = input().strip()
    sub_string = input().strip()
    print(count_substring(string, sub_string))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def count_substring(string: str, sub_string: str) -> int:
    count = 0
    sub_len = len(sub_string)
    for i in range(len(string) - sub_len + 1):
        if string[i:i + sub_len] == sub_string:
            count += 1
    return count
================================================================================
"""
