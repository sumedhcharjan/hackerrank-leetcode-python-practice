"""
================================================================================
CHALLENGE: Encode and Decode Strings (LeetCode 271 / Medium)
TRACK: 07_leetcode_hackerrank_medium
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Design an algorithm to encode a list of strings to a single string. The encoded string
is then sent over the network and decoded back to the original list of strings.

Please implement `encode` and `decode` methods such that `decode(encode(strs)) == strs`.

Notice that the strings may contain any possible ASCII characters (including spaces,
delimiters `#`, numbers, special symbols, newlines, etc.).

INPUT FORMAT:
A list of space-separated strings.

OUTPUT FORMAT:
Print True if the decoded array matches the original list of strings, else False.

SAMPLE INPUT 0:
lint code love you

SAMPLE OUTPUT 0:
True
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Encode and Decode Strings"
POINTS = 20

TEST_CASES = [
    {"input": "lint code love you\n", "expected": "True", "hidden": False},
    {"input": "hello #world 123#456\n", "expected": "True", "hidden": True}
]


def encode(strs: list) -> str:
    # Hint: Prefix each string with its length followed by a delimiter, e.g. "4#lint"
    pass


def decode(s: str) -> list:
    # Parse length prefix and extract substring
    pass


def solve():
    strs = input().split()
    encoded = encode(strs)
    decoded = decode(encoded)
    print(decoded == strs)


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def encode(strs: list) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(s: str) -> list:
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        res.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length
    return res
================================================================================
"""
