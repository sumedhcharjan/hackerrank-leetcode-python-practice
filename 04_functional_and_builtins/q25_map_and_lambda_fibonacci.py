"""
================================================================================
CHALLENGE: Map and Lambda Expression (Fibonacci)
TRACK: 04_functional_and_builtins
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
Let's learn about map and lambda functions!
You have to generate a list of the first N Fibonacci numbers, 0 being the first number.
Then, apply the lambda function to cube each Fibonacci number and print the list.

Fibonacci series starts: [0, 1, 1, 2, 3, 5, 8, 13, ...]

INPUT FORMAT:
An integer N.

CONSTRAINTS:
0 <= N <= 15

OUTPUT FORMAT:
A list on a single line containing the cubes of the first N Fibonacci numbers.

SAMPLE INPUT 0:
5

SAMPLE OUTPUT 0:
[0, 1, 1, 8, 27]
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Map and Lambda Expression (Fibonacci)"
POINTS = 10

TEST_CASES = [
    {"input": "5\n", "expected": "[0, 1, 1, 8, 27]", "hidden": False},
    {"input": "1\n", "expected": "[0]", "hidden": True},
    {"input": "0\n", "expected": "[]", "hidden": True}
]

cube = lambda x: x ** 3


def fibonacci(n: int) -> list:
    # return a list of fibonacci numbers up to n
    pass


def solve():
    n = int(input())
    print(list(map(cube, fibonacci(n))))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def fibonacci(n: int) -> list:
    if n == 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib
================================================================================
"""
