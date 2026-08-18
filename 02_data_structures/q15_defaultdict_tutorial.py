"""
================================================================================
CHALLENGE: DefaultDict Tutorial
TRACK: 02_data_structures
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
In this challenge, you will be given 2 integers, n and m. There are n words,
which might repeat, in group A. There are m words belonging to group B. For each
word in group B, check whether the word has appeared in group A or not. Print the
1-indexed positions of each occurrence of the word in group A. If it does not appear,
print -1.

INPUT FORMAT:
The first line contains n and m separated by a space.
The next n lines contain the words belonging to group A.
The next m lines contain the words belonging to group B.

CONSTRAINTS:
1 <= n <= 10000
1 <= m <= 100

SAMPLE INPUT 0:
5 2
a
a
b
a
b
a
b

SAMPLE OUTPUT 0:
1 2 4
3 5

EXPLANATION 0:
'a' appears at positions 1, 2, and 4 in group A.
'b' appears at positions 3 and 5 in group A.
================================================================================
"""

import sys
from pathlib import Path
from collections import defaultdict

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "DefaultDict Tutorial"
POINTS = 10

TEST_CASES = [
    {
        "input": "5 2\na\na\nb\na\nb\na\nb\n",
        "expected": "1 2 4\n3 5",
        "hidden": False
    }
]


def solve():
    # n, m = map(int, input().split())
    # d = defaultdict(list)
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    from collections import defaultdict
    n, m = map(int, input().split())
    d = defaultdict(list)
    for i in range(1, n + 1):
        word = input().strip()
        d[word].append(str(i))
    
    for _ in range(m):
        word = input().strip()
        if word in d:
            print(" ".join(d[word]))
        else:
            print("-1")
================================================================================
"""
