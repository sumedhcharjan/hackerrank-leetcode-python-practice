"""
================================================================================
CHALLENGE: Reverse Linked List (LeetCode 206 / HackerRank / Easy-Medium)
TRACK: 08_linked_lists_trees_and_recursion
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example:
Input:  1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1

Node Definition:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

INPUT FORMAT:
Space-separated integers representing nodes of the linked list.

OUTPUT FORMAT:
Space-separated integers of the reversed linked list.

SAMPLE INPUT 0:
1 2 3 4 5

SAMPLE OUTPUT 0:
5 4 3 2 1
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Reverse Linked List"
POINTS = 20

TEST_CASES = [
    {"input": "1 2 3 4 5\n", "expected": "5 4 3 2 1", "hidden": False},
    {"input": "1 2\n", "expected": "2 1", "hidden": False},
    {"input": "10\n", "expected": "10", "hidden": True}
]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    # Hint: Use prev, curr, next_node pointers to reverse links iteratively (or recursively)
    pass


def build_linked_list(arr: list) -> ListNode:
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_list_to_list(head: ListNode) -> list:
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


def solve():
    raw_input = input().strip()
    if not raw_input:
        print("")
        return
    arr = list(map(int, raw_input.split()))
    head = build_linked_list(arr)
    reversed_head = reverse_list(head)
    res_arr = linked_list_to_list(reversed_head)
    print(" ".join(map(str, res_arr)))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
================================================================================
"""
