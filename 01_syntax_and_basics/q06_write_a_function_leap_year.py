"""
================================================================================
CHALLENGE: Write a function (Leap Year)
TRACK: 01_syntax_and_basics
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
An extra day is added to the calendar almost every four years as February 29,
and the day is called a leap day. It corrects the calendar for the fact that the
Earth takes approximately 365.25 days to orbit the Sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:
- The year can be evenly divided by 4, is a leap year, UNLESS:
- The year can be evenly divided by 100, it is NOT a leap year, UNLESS:
- The year is also evenly divisible by 400. Then it IS a leap year.

This means that in the Gregorian calendar, the years 1900, 2100, 2200, 2300, 2500
and 2600 are NOT leap years, while 2000 and 2400 ARE leap years.

Task:
Given a year, determine whether it is a leap year. If it is a leap year, return
True, otherwise return False.

Note that the code stub reads from STDIN and calls your function `is_leap(year)`.

INPUT FORMAT:
A single integer, year.

CONSTRAINTS:
1900 <= year <= 10^5

OUTPUT FORMAT:
The function must return a Boolean value (True/False).

SAMPLE INPUT 0:
1990
SAMPLE OUTPUT 0:
False
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Write a function (Leap Year)"
POINTS = 10

TEST_CASES = [
    {"input": "1990\n", "expected": "False", "hidden": False},
    {"input": "2000\n", "expected": "True", "hidden": True},
    {"input": "2400\n", "expected": "True", "hidden": True},
    {"input": "1900\n", "expected": "False", "hidden": True},
    {"input": "2024\n", "expected": "True", "hidden": True},
]


def is_leap(year: int) -> bool:
    # Write your leap year determination logic here
    pass


def solve():
    year = int(input().strip())
    print(is_leap(year))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def is_leap(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
================================================================================
"""
