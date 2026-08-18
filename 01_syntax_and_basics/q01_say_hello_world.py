"""
================================================================================
CHALLENGE: Say Hello, World! With Python
TRACK: 01_syntax_and_basics
DIFFICULTY: Easy | POINTS: 5
================================================================================

PROBLEM STATEMENT:
Here is a sample line of code that can be executed in Python:
    print("Hello, World!")

You can just as easily store "Hello, World!" in a variable which you then print
to stdout:
    my_string = "Hello, World!"
    print(my_string)

Task:
Print "Hello, World!" to stdout.

INPUT FORMAT:
No input is required for this challenge.

OUTPUT FORMAT:
Print "Hello, World!" without quotes.

SAMPLE OUTPUT:
Hello, World!
================================================================================
"""

import sys
from pathlib import Path

# Add root directory to path to import test_helper
sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Say Hello, World! With Python"
POINTS = 5

TEST_CASES = [
    {
        "input": "",
        "expected": "Hello, World!",
        "hidden": False
    }
]


def solve():
    # Write your code inside this function
    # Hint: Use print() to display the required string
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    print("Hello, World!")
================================================================================
"""
