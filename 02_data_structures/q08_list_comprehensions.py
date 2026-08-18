"""
================================================================================
CHALLENGE: List Comprehensions
TRACK: 02_data_structures
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
Let's learn about list comprehensions! You are given three integers x, y and z
representing the dimensions of a cuboid along with an integer n. Print a list of
all possible coordinates (i, j, k) on a 3D grid where the sum of i + j + k is not
equal to n. Here:
    0 <= i <= x; 0 <= j <= y; 0 <= k <= z

Please use list comprehensions rather than multiple loops, as a learning exercise.

INPUT FORMAT:
Four integers x, y, z and n, each on a four separate lines.

CONSTRAINTS:
Print the list in lexicographical increasing order.

SAMPLE INPUT 0:
1
1
1
2

SAMPLE OUTPUT 0:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "List Comprehensions"
POINTS = 10

TEST_CASES = [
    {
        "input": "1\n1\n1\n2\n",
        "expected": "[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]",
        "hidden": False
    },
    {
        "input": "2\n2\n2\n2\n",
        "expected": "[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]",
        "hidden": True
    }
]


def solve():
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())
    # Hint: Use a single line list comprehension:
    # res = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ...]
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ans = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
    print(ans)
================================================================================
"""
