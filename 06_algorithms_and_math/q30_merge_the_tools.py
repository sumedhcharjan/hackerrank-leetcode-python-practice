"""
================================================================================
CHALLENGE: Merge the Tools!
TRACK: 06_algorithms_and_math
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Consider the following:
A string, s, of length n where s = c_0 c_1 ... c_{n-1}.
An integer, k, where k is a factor of n.

We can split s into n/k substrings where each substring, t_i, consists of a contiguous
block of k characters in s. Then, use each t_i to create string u_i such that:
- The characters in u_i are a subsequence of the characters in t_i.
- Any repeat occurrences of a character in t_i are removed from u_i (only the first
  occurrence of each character is kept).

Print u_0, u_1, ..., u_{n/k-1} each on a new line.

INPUT FORMAT:
The first line contains a single string, s.
The second line contains an integer, k, the length of each substring.

CONSTRAINTS:
1 <= n <= 10^5
1 <= k <= n

SAMPLE INPUT 0:
AABCAAADA
3

SAMPLE OUTPUT 0:
AB
CA
AD

EXPLANATION 0:
Substrings t0 = 'AAB' -> u0 = 'AB' (remove duplicate 'A')
t1 = 'CAA' -> u1 = 'CA' (remove duplicate 'A')
t2 = 'ADA' -> u2 = 'AD' (remove duplicate 'A')
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Merge the Tools!"
POINTS = 20

TEST_CASES = [
    {
        "input": "AABCAAADA\n3\n",
        "expected": "AB\nCA\nAD",
        "hidden": False
    }
]


def merge_the_tools(string: str, k: int):
    # Process string in chunks of length k and remove duplicates maintaining order
    pass


def solve():
    string, k = input(), int(input())
    merge_the_tools(string, k)


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def merge_the_tools(string: str, k: int):
    for i in range(0, len(string), k):
        sub = string[i:i + k]
        seen = []
        for ch in sub:
            if ch not in seen:
                seen.append(ch)
        print("".join(seen))
================================================================================
"""
