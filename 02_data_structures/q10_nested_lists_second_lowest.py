"""
================================================================================
CHALLENGE: Nested Lists (Second Lowest Grade)
TRACK: 02_data_structures
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
Given the names and grades for each student in a class of N students, store them in
a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their
names alphabetically and print each name on a new line.

INPUT FORMAT:
The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines:
- The first line contains a student's name (string).
- The second line contains their grade (float).

CONSTRAINTS:
2 <= N <= 5
There will always be one or more students having the second lowest grade.

OUTPUT FORMAT:
Print the name(s) of any student(s) having the second lowest grade in alphabetical
order, each on a new line.

SAMPLE INPUT 0:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

SAMPLE OUTPUT 0:
Berry
Harry
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Nested Lists (Second Lowest Grade)"
POINTS = 10

TEST_CASES = [
    {
        "input": "5\nHarry\n37.21\nBerry\n37.21\nTina\n37.2\nAkriti\n41\nHarsh\n39\n",
        "expected": "Berry\nHarry",
        "hidden": False
    },
    {
        "input": "4\nPrashant\n32\nKushal\n36\nHarsh\n39\nAnurag\n32\n",
        "expected": "Kushal",
        "hidden": True
    }
]


def solve():
    # students = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     students.append([name, score])
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    scores = sorted(list(set([s[1] for s in students])))
    second_lowest = scores[1]
    
    names = sorted([s[0] for s in students if s[1] == second_lowest])
    for name in names:
        print(name)
================================================================================
"""
