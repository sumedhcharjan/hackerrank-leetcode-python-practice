"""
================================================================================
CHALLENGE: String Validators
TRACK: 03_strings_and_regex
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
Python has built-in string validation methods for basic data. It can check if a
string is composed of alphabetical characters, alphanumeric characters, digits, etc.

Task:
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters,
alphabetical characters, digits, lowercase and uppercase characters.

Output Format:
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

SAMPLE INPUT 0:
qA2

SAMPLE OUTPUT 0:
True
True
True
True
True
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "String Validators"
POINTS = 10

TEST_CASES = [
    {
        "input": "qA2\n",
        "expected": "True\nTrue\nTrue\nTrue\nTrue",
        "hidden": False
    },
    {
        "input": "123\n",
        "expected": "True\nFalse\nTrue\nFalse\nFalse",
        "hidden": True
    }
]


def solve():
    # s = input()
    # Hint: Use any(c.isalnum() for c in s), any(c.isalpha() for c in s), etc.
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
================================================================================
"""
