"""
================================================================================
CHALLENGE: Finding the percentage
TRACK: 02_data_structures
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
The provided code stub will read in a dictionary containing key/value pairs of
name:[marks] for a list of students. Print the average of the marks array for the
student name provided, showing 2 decimal places.

INPUT FORMAT:
The first line contains the integer n, the number of students' records.
The next n lines contain the name and the marks obtained by a student separated by spaces.
The final line contains query_name, the name of a student to query.

CONSTRAINTS:
2 <= n <= 10
0 <= marks[i] <= 100
length of marks array = 3

OUTPUT FORMAT:
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

SAMPLE INPUT 0:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

SAMPLE OUTPUT 0:
56.00
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Finding the percentage"
POINTS = 10

TEST_CASES = [
    {
        "input": "3\nKrishna 67 68 69\nArjun 70 98 63\nMalika 52 56 60\nMalika\n",
        "expected": "56.00",
        "hidden": False
    },
    {
        "input": "2\nHarsh 25 26.5 28\nAnurag 26 28 30\nHarsh\n",
        "expected": "26.50",
        "hidden": True
    }
]


def solve():
    # n = int(input())
    # student_marks = {}
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()
    # Hint: Format using f"{avg:.2f}"
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    avg = sum(marks) / len(marks)
    print(f"{avg:.2f}")
================================================================================
"""
