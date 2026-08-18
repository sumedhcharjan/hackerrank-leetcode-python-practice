"""
================================================================================
CHALLENGE: Lists
TRACK: 02_data_structures
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
Consider a list (list = []). You can perform the following commands:
1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where
each command will be one of the 7 types listed above. Iterate through each command
in order and perform the corresponding operation on your list.

INPUT FORMAT:
The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

SAMPLE INPUT 0:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

SAMPLE OUTPUT 0:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Lists"
POINTS = 10

TEST_CASES = [
    {
        "input": "12\ninsert 0 5\ninsert 1 10\ninsert 0 6\nprint\nremove 6\nappend 9\nappend 1\nsort\nprint\npop\nreverse\nprint\n",
        "expected": "[6, 5, 10]\n[1, 5, 9, 10]\n[9, 5, 1]",
        "hidden": False
    }
]


def solve():
    # N = int(input())
    # arr = []
    # Process commands dynamically
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    N = int(input())
    arr = []
    for _ in range(N):
        cmd = input().split()
        op = cmd[0]
        args = cmd[1:]
        if op == "insert":
            arr.insert(int(args[0]), int(args[1]))
        elif op == "print":
            print(arr)
        elif op == "remove":
            arr.remove(int(args[0]))
        elif op == "append":
            arr.append(int(args[0]))
        elif op == "sort":
            arr.sort()
        elif op == "pop":
            arr.pop()
        elif op == "reverse":
            arr.reverse()
================================================================================
"""
