"""
================================================================================
CHALLENGE: String Split and Join
TRACK: 03_strings_and_regex
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
In Python, a string can be split on a delimiter.
Example:
    >>> a = "this is a string"
    >>> a = a.split(" ") # a is converted to a list of strings.
    >>> print a
    ['this', 'is', 'a', 'string']

And joining a list of strings:
    >>> a = "-".join(a)
    >>> print a
    this-is-a-string

Task:
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

INPUT FORMAT:
The one line contains a string consisting of space separated words.

OUTPUT FORMAT:
Print the formatted string.

SAMPLE INPUT 0:
this is a string

SAMPLE OUTPUT 0:
this-is-a-string
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "String Split and Join"
POINTS = 10

TEST_CASES = [
    {"input": "this is a string\n", "expected": "this-is-a-string", "hidden": False},
    {"input": "HackerRank Python Practice\n", "expected": "HackerRank-Python-Practice", "hidden": True}
]


def split_and_join(line: str) -> str:
    pass


def solve():
    line = input()
    print(split_and_join(line))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def split_and_join(line: str) -> str:
    words = line.split(" ")
    return "-".join(words)
================================================================================
"""
