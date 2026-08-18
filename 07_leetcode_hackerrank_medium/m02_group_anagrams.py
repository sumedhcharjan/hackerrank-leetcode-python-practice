"""
================================================================================
CHALLENGE: Group Anagrams (LeetCode 49 / Medium)
TRACK: 07_leetcode_hackerrank_medium
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given an array of strings `strs`, group the anagrams together. You can return the
answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

INPUT FORMAT:
A single line containing space-separated strings.

OUTPUT FORMAT:
Print each group of anagrams on a new line (sorted alphabetically within each group,
and groups sorted by their first element for consistent test output).

SAMPLE INPUT 0:
eat tea tan ate nat bat

SAMPLE OUTPUT 0:
ate eat tea
bat
nat tan
================================================================================
"""

import sys
from collections import defaultdict
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Group Anagrams"
POINTS = 20

TEST_CASES = [
    {
        "input": "eat tea tan ate nat bat\n",
        "expected": "ate eat tea\nbat\nnat tan",
        "hidden": False
    },
    {
        "input": "a\n",
        "expected": "a",
        "hidden": True
    }
]


def group_anagrams(strs: list) -> list:
    # Hint: Use a defaultdict(list) where the key is tuple(sorted(word))
    pass
    m={}
    for s in strs:
        key="".join(sorted(s))
        if key not in m:
            m[key]=[]
        m[key].append(s)
    ans=[]
    for _,value in m.items():
        ans.append(value)
    return ans

def solve():
    words = input().split()
    groups = group_anagrams(words)
    # Standardize output for comparison: sort words inside each group, then sort groups
    formatted_groups = [sorted(g) for g in groups]
    formatted_groups.sort(key=lambda g: g[0] if g else "")
    for g in formatted_groups:
        print(" ".join(g))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def group_anagrams(strs: list) -> list:
    ans = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        ans[key].append(s)
    return list(ans.values())
================================================================================
"""
