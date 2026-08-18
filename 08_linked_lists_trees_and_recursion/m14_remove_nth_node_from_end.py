"""
================================================================================
CHALLENGE: Remove Nth Node From End of List (LeetCode 19 / Medium)
TRACK: 08_linked_lists_trees_and_recursion
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given the head of a linked list, remove the n-th node from the end of the list and return its head.

Example:
Input:  head = 1 -> 2 -> 3 -> 4 -> 5, n = 2
Output: 1 -> 2 -> 3 -> 5

INPUT FORMAT:
First line: space-separated integers for linked list.
Second line: integer n.

OUTPUT FORMAT:
Space-separated integers of the modified linked list.

SAMPLE INPUT 0:
1 2 3 4 5
2

SAMPLE OUTPUT 0:
1 2 3 5
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Remove Nth Node From End of List"
POINTS = 20

TEST_CASES = [
    {"input": "1 2 3 4 5\n2\n", "expected": "1 2 3 5", "hidden": False},
    {"input": "1\n1\n", "expected": "", "hidden": False},
    {"input": "1 2\n1\n", "expected": "1", "hidden": True}
]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    # Hint: Use fast and slow pointers separated by n steps with a dummy node
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
    raw = input().strip()
    n = int(input())
    if not raw:
        print("")
        return
    arr = list(map(int, raw.split()))
    head = build_linked_list(arr)
    new_head = remove_nth_from_end(head, n)
    res_arr = linked_list_to_list(new_head)
    print(" ".join(map(str, res_arr)))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next
================================================================================
"""
