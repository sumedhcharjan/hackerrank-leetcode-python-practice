"""
================================================================================
CHALLENGE: Capitalize!
TRACK: 03_strings_and_regex
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
You are asked to ensure that the first and last names of people begin with a capital
letter in their passports. For example, alison heck should be capitalized correctly
as Alison Heck.

Given a full name, your task is to capitalize the name appropriately.

Note:
The string may contain multiple spaces between words or leading/trailing spaces.
Using str.title() converts "12abc" to "12Abc", which is incorrect! You must capitalize
each word individually while preserving all whitespace.

INPUT FORMAT:
A single line of input containing the full name, S.

CONSTRAINTS:
0 < len(S) < 1000

OUTPUT FORMAT:
Print the capitalized string, S.

SAMPLE INPUT 0:
chris alan

SAMPLE OUTPUT 0:
Chris Alan
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Capitalize!"
POINTS = 10

TEST_CASES = [
    {"input": "chris alan\n", "expected": "Chris Alan", "hidden": False},
    {"input": "12abc\n", "expected": "12abc", "hidden": True},
    {"input": "hello   world  lol\n", "expected": "Hello   World  Lol", "hidden": True}
]


def solve_capitalize(s: str) -> str:
    # Hint: Loop through words or use string.capitalize() on word chunks
    pass


def solve():
    s = input()
    print(solve_capitalize(s))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve_capitalize(s: str) -> str:
    for word in s.split():
        s = s.replace(word, word.capitalize())
    return s
================================================================================
"""
