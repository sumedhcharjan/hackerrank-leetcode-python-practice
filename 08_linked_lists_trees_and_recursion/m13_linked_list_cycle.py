"""
================================================================================
CHALLENGE: Linked List Cycle Detection (LeetCode 141 / Medium)
TRACK: 08_linked_lists_trees_and_recursion
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer.

Return True if there is a cycle in the linked list. Otherwise, return False.

Hint: Floyd's Tortoise and Hare algorithm (Fast and Slow Pointers).

INPUT FORMAT:
First line: space-separated integers for linked list nodes.
Second line: integer `pos` representing 0-indexed position where tail connects (-1 if no cycle).

OUTPUT FORMAT:
Print True if cycle exists, else False.

SAMPLE INPUT 0:
3 2 0 -4
1

SAMPLE OUTPUT 0:
True

EXPLANATION 0:
Tail node (-4) connects to node index 1 (value 2). Cycle exists.
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Linked List Cycle Detection"
POINTS = 20

TEST_CASES = [
    {"input": "3 2 0 -4\n1\n", "expected": "True", "hidden": False},
    {"input": "1 2\n0\n", "expected": "True", "hidden": False},
    {"input": "1\n-1\n", "expected": "False", "hidden": True}
]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode) -> bool:
    # Hint: Use slow pointer (1 step) and fast pointer (2 steps)
    pass


def solve():
    arr = list(map(int, input().split()))
    pos = int(input())
    
    if not arr:
        print(False)
        return
        
    nodes = [ListNode(x) for x in arr]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    if pos != -1:
        nodes[-1].next = nodes[pos]
        
    print(has_cycle(nodes[0]))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def has_cycle(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
================================================================================
"""
