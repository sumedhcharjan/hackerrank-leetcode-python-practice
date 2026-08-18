"""
================================================================================
CHALLENGE: Zipped!
TRACK: 04_functional_and_builtins
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
The National University conducts an examination of N students in X subjects.
Your task is to compute the average marks of each student.

Average score = Sum of scores in all subjects / Total number of subjects

The format of the input has marks grouped by subject! (First line contains all
student scores for subject 1, second line for subject 2, etc.)
You need to aggregate scores by student using `zip()`.

INPUT FORMAT:
The first line contains N (number of students) and X (number of subjects) separated by space.
The next X lines contain the space separated marks obtained by students in that subject.

OUTPUT FORMAT:
Print the averages of all students on separate lines, formatted to 1 decimal place.

SAMPLE INPUT 0:
5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90

SAMPLE OUTPUT 0:
90.0
91.0
82.0
90.0
85.3
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Zipped!"
POINTS = 10

TEST_CASES = [
    {
        "input": "5 3\n89 90 78 93 80\n90 91 85 88 86\n91 92 83 89 90\n",
        "expected": "90.0\n91.0\n82.0\n90.0\n85.3",
        "hidden": False
    }
]


def solve():
    # n, x = map(int, input().split())
    # scores = [list(map(float, input().split())) for _ in range(x)]
    # Hint: Use zip(*scores) to transpose subjects into student scores!
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    n, x = map(int, input().split())
    scores = [list(map(float, input().split())) for _ in range(x)]
    for student_marks in zip(*scores):
        print(f"{sum(student_marks) / len(student_marks):.1f}")
================================================================================
"""
